# Stori Challenge

This is a challenge for the stori company. It is focused on the management of banking transactions and notifications

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for testing purposes.

### Prerequisites

What things you need to install the software and how to install them:

- Docker
- Docker Compose

## Code Structure

This project follows a clean microservices-oriented architecture, ensuring separation of concerns and scalability. Below is an overview of the main directories and their roles within the application:

- `/config`: Contains configuration files that dictate the app's settings and environment variables.
- `/daos` (Data Access Objects): This directory includes scripts that contain database queries. These scripts are responsible for direct interactions with the database, perfor
- `/database`: Includes scripts related to database initialization, connection, and management.
- `/services`: Contains service classes that encapsulate the business logic of the application. These services orchestrate data flow between the DAOs and the endpoints.
- `/utils`: Utility scripts and helper functions that provide common functionality across the application.
- `/docker-compose.yml`: Defines the multi-container Docker application.
- `/Dockerfile`: Contains the commands a user could call on the command line to assemble an image.
- `/entrypoint.sh`: A script that runs as the Docker container is initialized. It is used to set up the environment and start the application.
- `/main.py`: The entry point to the Flask application. It defines the routes and starts the web server.
- `/Makefile`: A script for automating common development tasks such as starting the server, running migrations, etc.
- `/requirements.txt`: A file listing the Python dependencies that can be installed with `pip install -r requirements.txt`.
- `/txns.csv`: An example or default CSV file containing transaction data.
- `/wait-for-it.sh`: A script for controlling the order of service startup in docker-compose.

Each service within the `/services` directory is designed to run as an independent microservice, potentially allowing for easy scaling and independent deployment cycles.

### Installing

A step-by-step series of examples that tell you how to get a development environment running.

First, clone the repository to your local machine:
```bash
git clone https://github.com/Alkayzer/stori_challenge.git
```

Navigate to the cloned directory:
```bash
cd stori_challenge
```

Copy the .env.example file to .env and fill it with your own values:
```bash
cp .env.example .env
```

Now, start the services using Docker Compose:
```bash
docker-compose up -d
```

The application should now be running and accessible via http://localhost:5001.

## Consuming the API

### Using `curl`

To send a transaction file along with user details, use the following curl command:

```bash
curl --location 'http://127.0.0.1:5001/transaction' \
--form 'file=@"/path/to/your/txns.csv"' \
--form 'email="user@example.com"' \
--form 'full_name="Full Name"'
```

Replace "/path/to/your/txns.csv" with the path to your actual CSV file, and adjust the email and full_name form fields with the user's actual data.

### Using Postman

To consume the API using Postman:

1. Open Postman and create a new request.
2. Set the method to POST and the URL to http://127.0.0.1:5001/transaction.
3. In the 'Body' tab, select form-data.
4. Add the following key-value pairs:
   * file, select File from the dropdown and upload your CSV file.
   * email, set the value to the user's email, e.g., user@example.com.
   * full_name, set the value to the user's full name, e.g., Full Name.
5. Send the request.

## Author:
- Name: Marcelo Perez Britos.
- Linkedin: https://www.linkedin.com/in/marceloperezbritos/.
