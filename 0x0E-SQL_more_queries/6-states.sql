-- create database and table
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE states ( id INT UNIQUE NOT NULL PRIMARY KEY AUTO_INCREMENT,
                            name VARCHAR(256)  NOT NULL);
