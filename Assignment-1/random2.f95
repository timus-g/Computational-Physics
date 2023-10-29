program random_numbers_2
  implicit none
  real*8 :: r
  integer :: i,j,seed
  seed = 212
  open (unit=1, file="test_ran.dat", action="write")
  call srand(seed)
  do i = 1, 10
    r = rand()
    write(1,'(f12.10)') r
  end do
  write(1,*)"Changing seed and generating 10 new random numbers"
  seed= 3015
  call srand(seed)
  do i = 1, 10
    r = rand()
    write(1,'(f12.10)') r
  end do
end program random_numbers_2
