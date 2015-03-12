! LJcalc.f95 --- Calculates forces
subroutine LJcalc(R,n,Pnum, U)
implicit none
real(8), intent(in) :: Pnum
integer, intent(in) :: n
real(8), intent(in) :: R(n, 2)
real(8), intent(inout) :: U(n, 2)
!f2py intent(in, out) U
real(8) :: dr(2), dr2
real(8), parameter :: rmax = 3.2_8
integer :: i, j
do i = 0, Pnum
    do j = 1, i-1
        dr = R(i,:) - R(j,:)
        dr2 = sum(dr**2)
        U=4*(1/dr2**6 - 1/dr2**3)        
    end do
end do
end subroutine
