program random_numbers
  implicit none
  real*8 :: r,sums
  integer :: i,j,seed
  open(unit=1, file='dist_sum_random_2.dat', action ="write")
  do i=1, 10000
      sums=0.0d0
      seed = i
      call srand(seed)
	do j = 1, 10000
             r = 2.0d0*rand() - 1.0d0
	     sums=sums+r   
	end do
	write(1,*)sums
  end do 
  close(unit=1)
end program random_numbers

