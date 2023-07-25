-- Comando para listar las tablas de la base de datos
mysql -u "$MYSQL_USER" -p"$MYSQL_PASSWORD" -e "USE $DATABASE_NAME; SHOW TABLES;"
