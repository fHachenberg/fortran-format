import subprocess
from pathlib import Path
import tempfile
import argparse

'''
Reformats Fortran (f77, f90) source files.
'''

def run_fortran_format(input_args) -> int:
    '''
    args are literally the command line string args
    '''

    # argument parsing -------------------

    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('input_files', metavar='INPUT_FILE', type=str, nargs='+',
                        help='fortran files to process')
    parser.add_argument('--txl-arg', '-TXL', type=str, default=None, action="append", help="Arguments to pass on to TXL (for debug and test purposes mainly). If passed (with or without arguments), fortran-format outputs different details about the TXL call")

    output_args = parser.add_mutually_exclusive_group()
    output_args.add_argument('-o', '--outfile', metavar='FILE', type=str, default='STDOUT',
                             help='write result to file. If multiple input files were selected, the content is the concatenation of results for each input file. If FILE is `STDOUT`, the output is written to stdout. This is the default')
    output_args.add_argument('-i', '--inplace', action="store_true", default=False,
                             help='change all input files in place')
    # formatting options
    tab_opts = parser.add_argument_group('tab options')

    indent_opts = parser.add_argument_group('indentation options')
    indent_opts.add_argument('--indent-callables', action='store_true',
                             help='indent code inside subroutines and functions')
    indent_opts.add_argument('--indent-modules', action='store_true', help="indent code inside module block")
    indent_opts.add_argument('--indent-program', action='store_true', help="indent code inside program block")

    args = parser.parse_args(input_args)

    enable_txl_outputs = (args.txl_arg is not None)
    txl_program_file =  Path(__file__).parent / "fortran-format.txl"

    # clear out put file
    if args.outfile != "STDOUT":
        open(args.outfile, "wt").close()

    # txl execution -------------------

    for input_file in args.input_files:
        with tempfile.TemporaryFile() as tmpfile:
            txl_call = ['txl', input_file, str(txl_program_file)] + args.txl_arg
            print("TXL call:", " ".join(txl_call))
            stderr = subprocess.DEVNULL # by default we throw away stderr
            if enable_txl_outputs:
                stderr = None
            cproc = subprocess.run(txl_call, stdout=tmpfile, stderr=stderr)
            if cproc.returncode != 0:
                raise Exception("TXL ended with statuscode {}".format(cproc.returncode))
            tmpfile.seek(0)
            if args.outfile == "STDOUT":
                print(tmpfile.read().decode("utf8"))
            else:
                if args.inplace:
                    # if inplace, overwrite input file
                    outfilename, mode = input_file, "wb" # b because tempfile is opened with b
                else:
                    # if outfile is specified, append to it (is cleared at the start)
                    outfilename, mode = args.outfile, "ab" # b because tempfile is opened with b
                with open(outfilename, mode) as out:
                    out.write(tmpfile.read())

if __name__ == "__main__":

    import sys
    raise SystemExit(run_fortran_format(sys.argv))
