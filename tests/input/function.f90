module my_MODULE
contains
integer function a(x, y, o)
implicit none
      ! these are input args
  integer, intent(in) :: x, y ! <- we describe them here
end function
end module