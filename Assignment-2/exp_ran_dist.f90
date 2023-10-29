
program exp_random

 integer :: i,seed
 real*8 :: lambda, x, exponential_randoms
 open (unit=1, file = 'exp_ran_dist.dat', action = 'write')
 lambda = 2.0 ! rate parameter
 seed = 123456
 call srand(seed)
  do i = 1, 1000000
    x = ran()
    exponential_randoms = -log(1-x)/lambda
    write(1,'(f12.10)')exponential_randoms
  end do
    
end program exp_random
