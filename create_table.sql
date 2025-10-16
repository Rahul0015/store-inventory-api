-- create_tables.sql

-- Create database (optional if already exists)
CREATE DATABASE web_lab;

\c web_lab;

-- Create products table
CREATE TABLE IF NOT EXISTS products (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    category VARCHAR(255) NOT NULL,
    quantity INTEGER DEFAULT 0,
    price NUMERIC(10, 2) NOT NULL,
    sku VARCHAR(255) UNIQUE NOT NULL
);
