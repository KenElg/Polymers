! LJcalc.f95 --- Calculates forces
subroutine LJcalc(R,n,Pnum, U)
implicit none
real(8), intent(in) :: Pnum
integer, intent(in) :: n
real(8), intent(in) :: R(n, 2)
real(8), intent(inout) :: U
!f2py intent(in, out) U
real(8) :: dr(2), dr2
real(8), parameter :: eps = 0.25
real (8), parameter :: sig = 0.8
integer ::  j

    do j = 1, Pnum-2
       dr = R(Pnum,:) - R(j,:)
       dr2 = sum(dr**2)
       U=U + 4*eps*(sig**12/dr2**6 - sig**6/dr2**3)
            
    end do

end subroutine
