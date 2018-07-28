ccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
c      written by the UFO converter
ccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc

C     Parameters that should not be recomputed event by event.
C     
      IF(READLHA) THEN

        G = 2 * DSQRT(AS*PI)  ! for the first init

        MDL_CW = SQRT(DCMPLX(1.000000D+00-MDL_SW2))

        MDL_SQRT__SW2 = SQRT(DCMPLX(MDL_SW2))

        MDL_SW = MDL_SQRT__SW2

        MDL_COS__CABI = COS(MDL_CABI)

        MDL_CKM1X1 = MDL_COS__CABI

        MDL_SIN__CABI = SIN(MDL_CABI)

        MDL_CKM1X2 = MDL_SIN__CABI

        MDL_CKM1X3 = 0.000000D+00

        MDL_CKM2X1 = -MDL_SIN__CABI

        MDL_CKM2X2 = MDL_COS__CABI

        MDL_CKM2X3 = 0.000000D+00

        MDL_CKM3X1 = 0.000000D+00

        MDL_CKM3X2 = 0.000000D+00

        MDL_CKM3X3 = 1.000000D+00

        MDL_R__EXP__2 = MDL_R**2

        MDL_F__EXP__2 = MDL_F**2

        MDL_LAM2 = (2.445180D+02*SQRT(DCMPLX(1.000000D+00
     $   +MDL_R__EXP__2)))/(MDL_F*MDL_R*ACOS(1.000000D+00-6.051600D+04
     $   /MDL_F__EXP__2))

        MDL_XL = MDL_R__EXP__2/(1.000000D+00+MDL_R__EXP__2)

        MDL_XL__EXP__2 = MDL_XL**2

        MDL_D2 = -8.333333D-01+2.000000D+00*(1.000000D+00-MDL_XL)
     $   *MDL_XL+MDL_XL__EXP__2/2.000000D+00

        MDL_LAM2__EXP__2 = MDL_LAM2**2

        MDL_LAMPHI2PHI2 = -1.600000D+01*MDL_LAM2__EXP__2*MDL_R__EXP__2

        MDL_SQRT__2 = SQRT(DCMPLX(2.000000D+00))

        MDL_MH__EXP__2 = MDL_MH**2

        MDL_COMPLEXI = DCMPLX(0.000000D+00,1.000000D+00)

        MDL_CW__EXP__2 = MDL_CW**2

        MDL_R__EXP__3 = MDL_R**3

        MDL_SW__EXP__2 = MDL_SW**2

        MDL_SW__EXP__4 = MDL_SW**4

        MDL_SQRT__XL = SQRT(DCMPLX(MDL_XL))

        MDL_F__EXP__3 = MDL_F**3

        MDL_XL__EXP__1_5 = MDL_XL**1.500000D+00

        MDL_XL__EXP__2_5 = MDL_XL**2.500000D+00

        MDL_XL__EXP__3 = MDL_XL**3

        MDL_CONJG__CKM1X1 = CONJG(DCMPLX(MDL_CKM1X1))

        MDL_CONJG__CKM1X2 = CONJG(DCMPLX(MDL_CKM1X2))

        MDL_CONJG__CKM1X3 = CONJG(DCMPLX(MDL_CKM1X3))

        MDL_CONJG__CKM2X1 = CONJG(DCMPLX(MDL_CKM2X1))

        MDL_CONJG__CKM2X2 = CONJG(DCMPLX(MDL_CKM2X2))

        MDL_CONJG__CKM2X3 = CONJG(DCMPLX(MDL_CKM2X3))

        MDL_CONJG__CKM3X1 = CONJG(DCMPLX(MDL_CKM3X1))

        MDL_CONJG__CKM3X2 = CONJG(DCMPLX(MDL_CKM3X2))

        MDL_CONJG__CKM3X3 = CONJG(DCMPLX(MDL_CKM3X3))

        MDL_AEW = 1.000000D+00/AEWM1

        MDL_SQRT__AEW = SQRT(DCMPLX(MDL_AEW))

        MDL_EE = 2.000000D+00*MDL_SQRT__AEW*SQRT(DCMPLX(PI))

        MDL_G1 = MDL_EE/MDL_CW

        MDL_GW = MDL_EE/MDL_SW

        MDL_VSM = (1.607700D+02*MDL_SW)/MDL_EE

        MDL_G1__EXP__2 = MDL_G1**2

        MDL_GW__EXP__2 = MDL_GW**2

        MDL_XH = (5.000000D+00*MDL_G1*MDL_GW)/(4.000000D+00*(
     $   -MDL_G1__EXP__2+5.000000D+00*MDL_GW__EXP__2))

        MDL_G1I = MDL_G1*MDL_SQRT__2

        MDL_GWI = MDL_GW*MDL_SQRT__2

        MDL_LAMPHI4 = (-8.000000D+00*(MDL_G1__EXP__2+MDL_GW__EXP__2))
     $   /3.000000D+00+(1.600000D+01*MDL_LAM2__EXP__2*MDL_R__EXP__2)
     $   /3.000000D+00

        MDL_VSM__EXP__2 = MDL_VSM**2

        MDL_V = (MDL_F*ACOS(1.000000D+00-MDL_VSM__EXP__2/MDL_F__EXP__2)
     $   )/MDL_SQRT__2

        MDL_SH = (MDL_VSM__EXP__2*MDL_XH)/MDL_F__EXP__2

        MDL_V__EXP__2 = MDL_V**2

        MDL_LAM = MDL_MH__EXP__2/(2.000000D+00*MDL_V__EXP__2)

        MDL_LAMPHI2 = (2.000000D+00*MDL_MH__EXP__2)/MDL_V__EXP__2

        MDL_YB = (MDL_YMB*MDL_SQRT__2)/MDL_V

        MDL_YC = (MDL_YMC*MDL_SQRT__2)/MDL_V

        MDL_YDO = (MDL_YMDO*MDL_SQRT__2)/MDL_V

        MDL_YE = (MDL_YME*MDL_SQRT__2)/MDL_V

        MDL_YM = (MDL_YMM*MDL_SQRT__2)/MDL_V

        MDL_YS = (MDL_YMS*MDL_SQRT__2)/MDL_V

        MDL_YT = (MDL_YMT*MDL_SQRT__2)/MDL_V

        MDL_YTAU = (MDL_YMTAU*MDL_SQRT__2)/MDL_V

        MDL_YUP = (MDL_YMUP*MDL_SQRT__2)/MDL_V

        MDL_SH__EXP__2 = MDL_SH**2

        MDL_CH = SQRT(DCMPLX(1.000000D+00-MDL_SH__EXP__2))

        MDL_MUH = SQRT(DCMPLX(MDL_LAM*MDL_V__EXP__2))

        MDL_LAMHPHIPHIH = (-4.000000D+00*MDL_LAMPHI2)/3.000000D+00

        MDL_EE__EXP__2 = MDL_EE**2

        MDL_GWI__EXP__2 = MDL_GWI**2

        MDL_CH__EXP__2 = MDL_CH**2

      ENDIF
C     
C     Parameters that should be recomputed at an event by even basis.
C     
      AS = G**2/4/PI

      MDL_SQRT__AS = SQRT(DCMPLX(AS))

      MDL_G__EXP__2 = G**2

      MDL_G__EXP__3 = G**3

      MDL_G__EXP__4 = G**4

C     
C     Definition of the EW coupling used in the write out of aqed
C     
      GAL(1) = 3.5449077018110318D0 / DSQRT(AEWM1)
      GAL(2) = 1D0

