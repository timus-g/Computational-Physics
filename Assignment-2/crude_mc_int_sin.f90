program crude_mc_int_sin
	
	implicit none
	integer :: i,n
	real*8 :: p,crude_mc,x,func,sigma,var,length,actual
	length=2*asin(1.0d0)
	actual=2.0d0
	
	open(unit=1, file='sin_crude_mc.dat')
	
	!read the no of MC steps
	write(*,*)"Enter the value of no. of MC steps (n)"
	read(*,*)n
	
7	crude_mc = 0.0d0
	sigma = 0.0d0
	
	do i=1,n
	  call random_number(p)
	  x=length*p
	  crude_mc = crude_mc+func(x)
	  sigma=sigma+func(x)*func(x)
	end do
	
	crude_mc = crude_mc/real(n)
	sigma = sigma/real(n)
	var = sigma-crude_mc*crude_mc
	
	crude_mc = length*crude_mc
	var = length*sqrt(var/real(n))
	write(*,*)n,"",crude_mc,"",var
	
	write(1,*)n,",",crude_mc,",",abs(crude_mc-actual)
	
!	automation  
        n = n*10
        if (n .le. 1000000) goto 7 
!        end automation
        
end program crude_mc_int
        
        real*8 function func(x)
        ! evaluate f(x) = sin(x)
        implicit none
        real*8 :: x
        func = sin(x)
        end function
	
	
