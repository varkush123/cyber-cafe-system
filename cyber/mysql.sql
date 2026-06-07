CREATE DATABASE cyber;
USE cyber;

--login table
CREATE TABLE login (
    username VARCHAR(50) NOT NULL PRIMARY KEY,
    password VARCHAR(100) NOT NULL
);

INSERT INTO login (username, password)
VALUES ('varsha', '123');

--computer table

CREATE TABLE computers (
    computer_id INT NOT NULL,
    computer_name VARCHAR(50) NOT NULL,
    company VARCHAR(50) NOT NULL,
    type VARCHAR(50) NOT NULL,
    model_no VARCHAR(50) NOT NULL,
    series VARCHAR(50) NOT NULL,
    ram VARCHAR(20) NOT NULL
);

--customer table

CREATE TABLE cusd (
    id_type VARCHAR(20) NOT NULL,
    id_no VARCHAR(20) PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    age INT NOT NULL,
    mobile_no VARCHAR(15) NOT NULL,
    email VARCHAR(50) NOT NULL,
    address VARCHAR(100) NOT NULL,
    check_in_datetime DATETIME NOT NULL,
    time_spend_minutes INT NOT NULL,
    computer_id INT NOT NULL
);