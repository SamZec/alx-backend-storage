-- 4-store.sql - creates a trigger that decreases the quantity of an item after adding a new order.

delimiter |

CREATE TRIGGER t AFTER INSERT ON orders
FOR EACH ROW
BEGIN
    UPDATE items SET quantity = quantity - NEW.number
        WHERE NEW.item_name = items.name;
END;|

delimiter ;
