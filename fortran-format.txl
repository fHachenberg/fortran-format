include "fortran.grm"

%rule indend_statements
%    replace [

%rule indent_subroutine
%    replace [SubroutineSubprogram]
%        subroutine [SubroutineSubprogram]
%    by
%        subroutine [indent_statements]
%end rule

function main
    match [program] _ [program]
end function
