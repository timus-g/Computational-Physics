program variables
 implicit none
 !Declare data types
 character(len=15) :: name
 integer :: int_var
 real :: float_var
 double precision :: double_var
 
 name = "Sumit Ghosh"
 int_var = 5
 float_var = 3.14
 double_var = 2.71828
 
 write(*,*) "My name:                        ",name
 write(*,*) "A integer variable:  ",int_var
 write(*,*) "A floating point variable:   ",float_var
 write(*,*) "A double-precision variable: ",double_var
 
end program variables
