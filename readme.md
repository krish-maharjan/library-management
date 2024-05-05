# LibMange: A mono repo Microservice application built on django for Library Management

## Postman Documentation [Postman Documentation](https://documenter.getpostman.com/view/26802289/2sA35G52qb)

## Project Overview

LibMange is a comprehensive library management system designed using a microservice architecture. It focuses on providing modular and scalable solutions for user authentication, book catalog management, and book borrowing services within a library context. The goal is to streamline the processes of managing book inventories, user access, and lending operations efficiently and securely.

## Services

- **Auth Service**: Facilitates user registration, authentication, and authorization, ensuring secure access to the library's system.
- **Book Management Service**: Manages the complete lifecycle of books within the library, from cataloging new entries to updating or removing existing records.
- **Book Borrow Service**: Handles the borrowing processes, including tracking the status of borrowed books and managing returns and due dates.

## Key Features

- Modular and scalable microservice design.
- Secure authentication and user management.
- Comprehensive book inventory management.
- Efficient tracking of borrowing and return processes.

## Technologies and Requirements

LibMange leverages Django and Django REST Framework, along with other technologies, to provide a robust and flexible platform:

- djangorestframework
- django-rest-knox
- pika

## Getting Started

Begin by setting up the environment for each service in the LibMange system by following these steps:

1. **Clone the Repository**

2. **Install Dependencies**
Within each service directory (`auth`, `book-management`, `book-borrow`), install the required packages from `requirements.txt`.

3. **Apply Database Migrations**
Execute database migrations for each service to prepare the database schema.
