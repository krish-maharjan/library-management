# LibMange: A Django Microservice Architecture for Library Management

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

- Django==5.0.3: For web application development and database management.
- djangorestframework==3.15.0: To create Web APIs for service communication.
- django-rest-knox==4.2.0: Provides token-based authentication for secure access.
- django-rest-passwordreset==1.4.0: Adds password reset functionality for users.
- pika==1.3.2: Integrates RabbitMQ messaging for service-to-service communication.
- And other necessary libraries for optimal performance.

## Getting Started

Begin by setting up the environment for each service in the LibMange system by following these steps:

1. **Clone the Repository**

