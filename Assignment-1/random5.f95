program random_numbers
  implicit none
  real*8 :: r,sums
  integer :: i,j,seed
  open(unit=1, file='dist_sum_random.dat', action ="write")
  do i=1, 10000
      sums=0.0d0
      seed = i
      call srand(seed)
	do j = 1, 10000
             r = rand()
	     sums=sums+r   
	end do
	write(1,*)sums
  end do 
  close(unit=1)
end program random_numbers
