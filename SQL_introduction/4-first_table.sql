--Write a script that creates a table called first_table in the current database in your MySQL server.
CREATE_TABLE_SQL="CREATE TABLE IF NOT EXISTS $TABLE_NAME (
    id INT,
    name VARCHAR(256)
);
