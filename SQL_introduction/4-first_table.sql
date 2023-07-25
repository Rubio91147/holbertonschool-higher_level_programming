--Write a script that creates a table called first_table in the current database in your MySQL server.
CREATE_TABLE_SQL="IF NOT EXISTS first_TABLE (
    id INT,
    name VARCHAR(256)
);
