-- CREATE SCHEMA

DROP DATABASE flask_users;

CREATE SCHEMA IF NOT EXISTS flask_users DEFAULT CHARACTER SET utf8;

USE flask_users;

-- CREATE FRIENDS TABLE

CREATE TABLE IF NOT EXISTS users (
	user_id     INTEGER       NOT NULL    AUTO_INCREMENT PRIMARY KEY,
	first_name  VARCHAR(25)   NOT NULL,
	last_name   VARCHAR(25)   NOT NULL,
	status      VARCHAR(45)   NOT NULL    DEFAULT 'Normal User',
	email       VARCHAR(45)   NOT NULL,
	password    VARCHAR(255)  NOT NULL,
	created_at  DATETIME      NOT NULL    DEFAULT NOW(),
	updated_at  DATETIME      NOT NULL    DEFAULT NOW()  ON UPDATE NOW()
);

