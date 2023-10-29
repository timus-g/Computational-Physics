program random_walk
    implicit none
    integer :: i,j,seed,sum,random_number
    real*8:: random_value,excluded_num
    excluded_num = 0.050
    open(unit=1, file="dist_sum_random_walk_3.csv", action = "write")
    call srand(seed)
    do i = 1, 100000
    seed = i
    sum = 0
	    do j = 1, 100000
	        do
                 random_value = rand()
                 if (random_value .ne. excluded_num) exit
                end do
		if (random_value < 0.5d0) then
		    random_number = -1
		else 
		    random_number = 1
		end if
		sum = sum + random_number        
	    end do
    	write(1,*)sum
    end do  
end program random_walk
