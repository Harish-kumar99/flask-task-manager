
# Flask Task Manager App

## Overview

This Flask Task Manager App is designed to help you manage your tasks efficiently. It provides a set of APIs for creating, updating, deleting, and retrieving tasks. The app also features a user registration and login system with password encryption for enhanced security. Logging and proper error messages are implemented to ensure a smooth user experience. Additionally, sensitive information such as secret keys is managed using a `.env` file. The entire project is dockerized, allowing for easy deployment with custom ports.

## Features

- **Task Management:**
  - Create tasks
  - Update task details
  - Delete tasks
  - Retrieve task information

- **User Authentication:**
  - User registration
  - User login

- **Security:**
  - Passwords are securely encrypted

- **Logging:**
  - Comprehensive logging for better debugging and monitoring

- **Error Handling:**
  - Proper error messages for a user-friendly experience

- **Configuration:**
  - Sensitive information stored in a `.env` file

- **Dockerized:**
  - Project is containerized for easy deployment
  - Custom ports for flexibility

## Getting Started

### Prerequisites

- Docker installed on your machine
- [Python](https://www.python.org/downloads/) installed

### Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/flask-task-manager.git
   ```

2. Navigate to the project directory:
   ```bash
   cd flask-task-manager
   ```

3. Create a `.env` file with your secret keys:
   ```env
   SECRET_KEY=your_secret_key
   DATABASE_URL=your_database_url
   ```

4. Build and run the Docker container:
   ```bash
   docker-compose up --build
   ```

