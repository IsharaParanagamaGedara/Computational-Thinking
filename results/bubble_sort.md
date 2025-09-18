BEGIN
    INPUT Array A of size n
    
    FOR i = 0 TO n-1 DO
        FOR j = 0 TO n-i-2 DO
            IF A[j] > A[j+1] THEN
                SWAP A[j] and A[j+1]
            ENDIF
        ENDFOR
    ENDFOR

    OUTPUT A
END
