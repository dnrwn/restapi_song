CREATE DATABASE IF NOT EXISTS your_database;
CREATE USER 'new_user'@'%' IDENTIFIED BY 'new_password';
GRANT ALL PRIVILEGES ON your_database.* TO 'new_user'@'%';
FLUSH PRIVILEGES;
