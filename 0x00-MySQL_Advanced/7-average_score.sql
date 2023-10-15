-- 7-average_score.sql - creates a stored procedure ComputeAverageScoreForUser that computes and store the average score for a student.

delimiter |

CREATE PROCEDURE ComputeAverageScoreForUser (IN user_id INT)
BEGIN
    DECLARE n FLOAT DEFAULT 0.0;
    SELECT AVG(score) INTO n FROM corrections
    WHERE corrections.user_id = user_id;
    UPDATE users SET average_score = n WHERE users.id = user_id;
END;|

delimiter ;
