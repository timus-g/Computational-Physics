program test_random
    implicit none
    integer :: i,j,seed
    real*8 :: rn(10,10),sums(1,10)
    open(unit=10, file='test_ran_10_seeds.dat', action ="write")
    do i = 1, 10
        seed = 100*i+10*i+i
        sums(1,i)=0.0d0
        call srand(seed)
        do j = 1, 10
            rn(i,j)=rand() 
            sums(1,i)=sums(1,i)+rn(i,j)          
        end do       
    end do
    write(10, '(10f12.8)') rn
    write(10, *)"NOW calculating average of 10 random numbers:"
    write(10, '(10f12.8)')sums/10.0d0 
    close(unit=10)
end program test_random

