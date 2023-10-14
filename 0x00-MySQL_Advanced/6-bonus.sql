-- 6-bonus.sql - creates a stored procedure AddBonus that adds a new correction for a student.

delimiter |

CREATE PROCEDURE AddBonus (
	IN user_id INT, IN project_name CHAR(255), IN score INT)
BEGIN
    IF project_name NOT IN (SELECT name FROM projects) THEN
	INSERT INTO projects (name) VALUES(project_name);
	SET @project_py = LAST_INSERT_ID();
	INSERT INTO corrections (user_id, project_id, score)
	    VALUES (user_id, @project_py, score);
    ELSE
	SELECT id INTO @project_id FROM projects
	    WHERE name = project_name LIMIT 1; 
	INSERT INTO corrections (user_id, project_id, score)
	    VALUES (user_id, @project_id, score);
    END IF;
    
END;|

delimiter ;
