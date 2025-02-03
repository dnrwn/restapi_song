CREATE DATABASE IF NOT EXISTS new_db;
USE new_db;
CREATE TABLE IF NOT EXISTS item (
    idx int(2) NOT NULL AUTO_INCREMENT PRIMARY KEY,
    input_1 int(2) DEFAULT NULL,
    input_2 varchar(5) DEFAULT NULL,
    input_3 varchar(10) DEFAULT NULL,
    input_4 BOOLEAN DEFAULT NULL,
    Create_date varchar(255) DEFAULT NULL,
    Update_date varchar(255) DEFAULT NULL
);
