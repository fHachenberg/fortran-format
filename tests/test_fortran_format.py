import pytest
import fortran_format
from pathlib import Path
from typing import List
import tempfile

import subprocess

@pytest.mark.parametrize("args,inputfile,expectedfile,expectedcmt", [
    (["--indent-callables"], "subroutine.f90", "indentation_subroutine.f90", "the subroutine/function statement itself shall not be indented!")
])
def test_fortran_format(args: List, inputfile: str, expectedfile: str, expectedcmt: str):
    '''
    Runs fortran-format on inputfile, using args and requires that the result is equal to expectedfile
    '''
    full_inputfile_path: Path = Path(__file__).parent / "input" / inputfile
    full_expectedfile_path = Path(__file__).parent / "expected" / expectedfile

    # to detect syntax errors in the input file, we first run gfortran on it
    cproc = subprocess.run(['gfortran', '-c', str(full_inputfile_path)], stderr=subprocess.PIPE)
    print(cproc.stderr.decode("utf8"))
    assert cproc.returncode == 0

    print(expectedcmt) # describe the exptected outcome
    with tempfile.NamedTemporaryFile() as tmpfile:
        fortran_format.run_fortran_format(args + [str(full_inputfile_path), "-o", tmpfile.name, "--txl-arg=-Dparse", "--txl-arg=-v"])
        print("comparing:", tmpfile.name, full_expectedfile_path)
        subprocess.run(['meld', str(full_expectedfile_path), tmpfile.name])
        with full_expectedfile_path.open("rt") as f_ref, open(tmpfile.name, "rt") as f_new:
            assert f_new.read() == f_ref.read()
