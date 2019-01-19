module my_MODULE
contains
function a(x, y, o)
    implicit none
    ! these are input args
    integer, intent(in) :: x, y ! <- we describe them here
    integer, intent(out) :: o
end function
end module