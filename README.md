## Product Seller Project
This project is an api which allows you to Register user, Login
Logout, change password and Create Product.

## Table of Contents
we have:
-Backend which is in DRF -Django Rest Framework-.
-Database Postgres.
-Docker for containerization


## Description
The project is for products which could be filtered by user.
and is ordered by price

## Instructions
- open the product seller directory.
- make build
  -to build the images.
- make sync
  - to make mgrations
- make up
  - To start the containers
  - The service will start at http://127.0.0.1:8000/api/v1/
  - To work with products http://127.0.0.1:8000/api/v1/products
  - To work with user
        -http://127.0.0.1:8000/api/v1/auth_api/register
        -http://127.0.0.1:8000/api/v1/auth_api/login
        -http://127.0.0.1:8000/api/v1/auth_api/logout
        -http://127.0.0.1:8000/api/v1/auth_api/password_change

- make test
  - To run the tests
- make superuser
  - To create super user
- make down
  - To stop containers


## Technologies used
- Django  
- DRF
- Docker  
- PostgreSQL


## Author
Mohamed Elsayed
