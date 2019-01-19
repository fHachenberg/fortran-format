#!/bin/bash

set -e

scriptdir=$(readlink -e $(dirname $BASH_SOURCE))

txl=/home/fabian/Programme/txl10.7.linux64/bin/txl
txl_prog=$scriptdir/fortran.txl

for f in examples/*.f90
do
	gfortran $f -c -o /dev/null
	$txl $f $txl_prog -Dparse -comment
done
