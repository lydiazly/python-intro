program test_read_stream
real(8) :: var1, arr(3, 2)
integer :: var2

open(31, file='../data/data_fortran2.dat',status='old', access='stream', form="unformatted")
read(31) var1
read(31) var2
read(31) arr

write(*, '(1x,f4.1,f4.1)') var1, var2
write(*, '(1x,f4.1,f4.1,f4.1)') arr(:,1)
write(*, '(1x,f4.1,f4.1,f4.1)') arr(:,2)
write(*, '(1x,a,f4.1)') 'arr(2, 1) = ', arr(2, 1)

end