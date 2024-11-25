CREATE DATABASE nutri_food;
CREATE USER herelius WITH PASSWORD '123456';
ALTER ROLE herelius SET client_encoding TO 'utf8';
ALTER ROLE herelius SET default_transaction_isolation TO 'read committed';
ALTER ROLE herelius SET timezone TO 'Europe/Paris';
GRANT ALL PRIVILEGES ON DATABASE nutri_food TO herelius;
