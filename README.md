# fortran-format
Reformats Fortran code, just like AStyle for C++.

## mission

There was a time when people spent a lot of time arguing about what kind of code style is both readable and easy to use. And they spent a lot of time correcting formatting errors in their and their colleagues' files. With the advent of auto formatters, those times are over fortunately. Today in most languages you can simply reformat all of your codebase uniformly in a matters of seconds.
This tool tries to achieve this new baseline for Fortran.

## install

- download TXL at https://www.txl.ca/txl-download.html
- put `bin` dir of TXL installation into your PATH
	
## usage

You have to call `fortran-format` on each individual Fortran code file. You can decide whether you want to write the result to stdout (neither `-o` nor `-i`), provide an output filename (`-o`) or let fortran-format change the file in place (`-i`).

	format-format <input file> [-o output file | -i ] [ args ... ]

To see a list of all available formatting options as well as other arguments, please run 

	fortran-format --help

## technical details
	
- The tools is based on TXL: https://www.txl.ca
- The Fortran grammar in fortran.grm is a modified version of 

	https://www.txl.ca/examples/Grammars/Fortran/Fortran.tar.gz
