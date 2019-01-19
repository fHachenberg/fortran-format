% Simple test of TXL Fortan 77 / 90 Grammar
% J.R. Cordy, Queen's University
% September 2009

include "fortran.grm"

% rule global_var_to_arg routine 
% 	replace [statement]
%	
% end rule

function main
    match [program] _ [program]
end function
