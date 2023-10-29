program random_numbers_avg
  implicit none
  real*8 :: r,sums
  integer :: i,seed
  open(unit=2, file='test_ran_avg.dat', action ="write")
  sums=0.0d0
  seed = 128
  call srand(seed)
  do i = 1, 100
    r = rand()
    sums=sums+r   
  end do
  write(2,*)"The average of 10^2 random numbers is:"
  write(2,'(f13.10)')sums/100.0d0
  write(2,*)"The difference between the mean value and 0.50d0 is:"
  write(2,'(f13.10)')abs(sums/100.0d0 - 0.50d0)
  write(2,*)" "
  sums=0.0d0
  seed = 351
  call srand(seed)
  do i = 1, 10000
    r = rand()
    sums=sums+r   
  end do
  write(2,*)"The average of 10^4 random numbers is:"
  write(2,'(f13.10)') sums/10000.0d0
  write(2,*)"The difference between the mean value and 0.50d0 is:"
  write(2,'(f13.10)')abs(sums/10000.0d0 - 0.50d0)
  write(2,*)" "
  sums=0.0d0
  seed = 796
  call srand(seed)
  do i = 1, 1000000
    r = rand()
    sums=sums+r   
  end do
  write(2,*)"The average of 10^6 random numbers is:"
  write(2,'(f13.10)') sums/1000000.0d0 
  write(2,*)"The difference between the mean value and 0.50d0 is:"
  write(2,'(f13.10)')abs(sums/1000000.0d0 - 0.50d0) 
  
  close(unit=2)
end program random_numbers_avg
