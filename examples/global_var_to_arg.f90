! vor module
module m
! nach module stmt
	integer :: a
	real :: b			
end module
! nach module block

! zwischen mod und prog


! vor program
program & ! hohoho
	global_var_to_arg

	integer :: luo = &
	1 
		! fdhhgjjhtff hfh
100 format (A10,X,X,F10.6)

	write (luo, 100) "hello", &   ! hohoho
					 5, &
					 "what the hell" // &
					 "not what i wanted"

	contains
	! vor subroutine
	subroutine subr(o)
		! nach subroutine
		use m
		! nach use
		implicit none
		! nach implicit none
		! vor o
		integer, intent(out) :: o ! ok
		o = a + (5 &
		* 5)	
	end subroutine
end program
! nach program
