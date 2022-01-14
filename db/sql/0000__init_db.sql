CREATE ROLE nutsnbolts WITH CREATEDB LOGIN;
ALTER ROLE nutsnbolts WITH PASSWORD 'nutsnbolts';
ALTER ROLE nutsnbolts SET client_encoding TO 'utf8';
ALTER ROLE nutsnbolts SET default_transaction_isolation TO 'read committed';

-- CREATE DATABASE nutsnbolts;
GRANT ALL PRIVILEGES ON DATABASE nutsnbolts TO nutsnbolts;
