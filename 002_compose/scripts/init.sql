CREATE USER dev PASSWORD 'dev';
CREATE DATABASE tutorial;
GRANT ALL PRIVILEGES ON DATABASE tutorial TO dev;

CREATE SCHEMA test;

CREATE TABLE test.names (
    id INT,
    name TEXT
);
