program random_numbers
  implicit none
  real*8 :: r
  integer :: i,seed
  seed = 1
  call srand(seed)
  do i = 1, 10
    r = rand()
    write(*,*) r
  end do
end program random_numbers

