program test_read_seq
real(8) :: var1, arr(3, 2)
integer(8) :: var2

open(31, file='../data/data_fortran1-1.dat',status='old', form="unformatted")
read(31) var1
read(31) var2
read(31) arr
close(31)
write(*, '(1x,a)'), 'data_fortran1-1.dat'
write(*, '(1x,f5.1,f5.1)') var1, var2
write(*, '(1x,f5.1,f5.1,f5.1)') arr(:,1)
write(*, '(1x,f5.1,f5.1,f5.1)') arr(:,2)
write(*, '(1x,a,f5.1)') 'arr(2, 1) = ', arr(2, 1)

open(32, file='../data/data_fortran1-2.dat', status='old', form="unformatted")
read(32) var1, var2, arr
close(32)
write(*, '(/1x,a)'), 'data_fortran1-2.dat'
write(*, '(1x,f5.1,f5.1)') var1, var2
write(*, '(1x,f5.1,f5.1,f5.1)') arr(:,1)
write(*, '(1x,f5.1,f5.1,f5.1)') arr(:,2)
write(*, '(1x,a,f5.1)') 'arr(2, 1) = ', arr(2, 1)

end