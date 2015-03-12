! forcetestken.f95 --- Calculates forces
subroutine Force(R,tf,n,L)
implicit none
real(8), intent(in) :: L
integer, intent(in) :: n
real(8), intent(in) :: R(n, 3)
real(8), intent(inout) :: tf(n, 3)
!f2py intent(in, out) tf
real(8) :: dr(3), dr2, F
real(8), parameter :: rmax = 3.2_8
integer :: i, j
tf = 0._8
do i = 0, n
    do j = 1, i-1
        dr = R(i,:) - R(j,:)
        dr = dr - nint(dr/L)*L
        dr2 = sum(dr**2)
        if (dr2<rmax**2) then
            F=24*(2/dr2**7 - 1/dr2**4)
            if (F>1000._8) print *, i, j, dr2
            tf(i,:) = tf(i,:) + F*dr
            tf(j,:) = tf(j,:) - F*dr
        end if
    end do
end do
end subroutine
