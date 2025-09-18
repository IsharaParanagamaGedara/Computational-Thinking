BEGIN
    INPUT number_of_readings (N)
    CREATE empty list MaxValues

    FOR reading_index = 1 TO N DO
        INPUT Reading[8][8]
        SET max_height = Reading[0][0]

        FOR row = 0 TO 7 DO
            FOR col = 0 TO 7 DO
                IF Reading[row][col] > max_height THEN
                    SET max_height = Reading[row][col]
                ENDIF
            ENDFOR
        ENDFOR

        APPEND max_height TO MaxValues
    ENDFOR

    SET total = 0
    FOR i = 0 TO LENGTH(MaxValues) - 1 DO
        total = total + MaxValues[i]
    ENDFOR

    average = total / LENGTH(MaxValues)

    OUTPUT "Average of maximum heights = ", average
END
