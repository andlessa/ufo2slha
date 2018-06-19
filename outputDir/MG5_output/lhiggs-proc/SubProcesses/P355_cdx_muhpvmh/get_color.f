      FUNCTION GET_COLOR(IPDG)
      IMPLICIT NONE
      INTEGER GET_COLOR, IPDG

      IF(IPDG.EQ.-8880014)THEN
        GET_COLOR=1
        RETURN
      ELSE IF(IPDG.EQ.-8880013)THEN
        GET_COLOR=1
        RETURN
      ELSE IF(IPDG.EQ.-24)THEN
        GET_COLOR=1
        RETURN
      ELSE IF(IPDG.EQ.-4)THEN
        GET_COLOR=-3
        RETURN
      ELSE IF(IPDG.EQ.-1)THEN
        GET_COLOR=-3
        RETURN
      ELSE IF(IPDG.EQ.1)THEN
        GET_COLOR=3
        RETURN
      ELSE IF(IPDG.EQ.4)THEN
        GET_COLOR=3
        RETURN
      ELSE IF(IPDG.EQ.24)THEN
        GET_COLOR=1
        RETURN
      ELSE IF(IPDG.EQ.8880013)THEN
        GET_COLOR=1
        RETURN
      ELSE IF(IPDG.EQ.8880014)THEN
        GET_COLOR=1
        RETURN
      ELSE IF(IPDG.EQ.7)THEN
C       This is dummy particle used in multiparticle vertices
        GET_COLOR=2
        RETURN
      ELSE
        WRITE(*,*)'Error: No color given for pdg ',IPDG
        GET_COLOR=0
        RETURN
      ENDIF
      END
