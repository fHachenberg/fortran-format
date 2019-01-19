# fortran-format
Reformats Fortran code, just like AStyle for C++.

## mission

There was a time when people spent a lot of time arguing about what kind of code style is both readable and easy to use. And they spent a lot of time correcting formatting errors in their and their colleagues' files. With the advent of auto formatters, those times are over fortunately. Today in most languages you can simply reformat all of your codebase uniformly in a matters of seconds.
This tool tries to achieve this new baseline for Fortran.

## supported Fortran versions

The parser we use can parse Fortran 90. This already involves a large amount of what is normally used in today's Fortran programms (`TYPE`, `INTENT`, ...). In the future I plan to extend the parser to Fortran 2003 or even 2008.

## install

- download TXL at https://www.txl.ca/txl-download.html
- put `bin` dir of TXL installation into your `PATH`
	
## usage

You can call `fortran-format` on each individual Fortran code file or a list of them (i.e. use glob expression like `*.f90`). `fortran-format` can either write the result (for each file) to stdout (neither `-o` nor `-i`), to a specific output file (`-o`. Only valid if you pass exactly one filename) or change the file(s) in place (`-i`).

	format-format <input files> [-o output file | -i ] [ args ... ]

To see a list of all available formatting options as well as other arguments, please run 

	fortran-format --help

## technical details
	
- The tools is based on TXL: https://www.txl.ca
- The Fortran grammar in fortran.grm is a modified version of 

	https://www.txl.ca/examples/Grammars/Fortran/Fortran.tar.gz
