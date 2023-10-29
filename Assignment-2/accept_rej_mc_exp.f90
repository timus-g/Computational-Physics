program accept_rej
	!program to evaluate I=Int_0_3 exp(x) dx
	
	implicit none
	integer :: i,n,pt_curve
	real*8 :: x,p,y,integral,exact
	
	open(unit=1, file='exp_accept_rej_mc.dat')
	
	!read the no of MC steps
	write(*,*)"Enter the value of no. steps (n)"
	read(*,*)n
	
7	pt_curve = 0
	do i=1,n
	
	  ! find random value of "x" between 0 and 3
	  
	  call random_number(p)
	  y=exp(3.0)*p
	  
	  ! if y at exp(y) is below the curve we accept
	  if (y .lt. exp(x)) then
	   pt_curve = pt_curve+1
	  end if
	  
	end do
	
!	multiply with the area of rectangle and divide by the no. of cycles
	
	integral = 3.0d0*exp(3.0)*real(pt_curve)/real(n)
	exact = exp(3.0)-1.0d0
	
	write(1,*)n,",",integral,",",abs(integral-exact)
	
!	automation  
        n = n*10
        if (n .le. 1000000) goto 7 
!        end automation
        
end program accept_rej
        
        real*8 function func(x)
        ! evaluate f(x) = exp(x)
        implicit none
        real*8 :: x
        func = exp(x)
        end function
        
        
