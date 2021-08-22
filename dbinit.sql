CREATE DATABASE IF NOT EXISTS textitsearchit;

USE textitsearchit;


CREATE USER IF NOT EXISTS cameron;
GRANT CREATE ON DATABASE textitsearchit TO cameron;

DROP SCHEMA IF EXISTS cameron_schema CASCADE;
CREATE SCHEMA cameron_schema AUTHORIZATION cameron;

CREATE TABLE textitsearchit.users (
    phone_number STRING PRIMARY KEY,
    options STRING[],
    t STRING
);

