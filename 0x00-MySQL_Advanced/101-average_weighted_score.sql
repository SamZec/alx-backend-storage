-- 101-average_weighted_score.sql
-- creates a stored procedure ComputeAverageWeightedScoreForUsers
-- computes and store the average weighted score for all students.

delimiter |

DROP PROCEDURE IF EXISTS ComputeAverageWeightedScoreForUsers;
CREATE PROCEDURE ComputeAverageWeightedScoreForUsers ()
BEGIN
    UPDATE users set average_score = (SELECT
    SUM(corrections.score * projects.weight) / SUM(projects.weight)
    FROM corrections
    INNER JOIN projects
    ON projects.id = corrections.project_id
    WHERE corrections.user_id = users.id);
END;|

delimiter ;
