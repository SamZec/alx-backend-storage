-- 10-div.sql -  creates a function SafeDiv that divides (and returns) the first by the second number
-- returns 0 if the second number is equal to 0.

delimiter |

CREATE FUNCTION SafeDiv (a INT, b INT)
RETURNS FLOAT(50) DETERMINISTIC
BEGIN
    IF b = 0 THEN
	RETURN 0;
    ELSE
	RETURN a / b;
    END IF;
END;|

delimiter ;
