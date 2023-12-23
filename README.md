# Deploy a Python (Flask) web app to Azure App Service - Sample Application

This is the sample Flask application for the Azure Quickstart [Deploy a Python (Django or Flask) web app to Azure App Service](https://docs.microsoft.com/en-us/azure/app-service/quickstart-python). For instructions on how to create the Azure resources and deploy the application to Azure, refer to the Quickstart article.

Sample applications are available for the other frameworks here:

* Django [https://github.com/Azure-Samples/msdocs-python-django-webapp-quickstart](https://github.com/Azure-Samples/msdocs-python-django-webapp-quickstart)
* FastAPI [https://github.com/Azure-Samples/msdocs-python-fastapi-webapp-quickstart](https://github.com/Azure-Samples/msdocs-python-fastapi-webapp-quickstart)

If you need an Azure account, you can [create one for free](https://azure.microsoft.com/en-us/free/).




## Manual Setup Instructions

Follow these steps to manually set up the environment and run the application.

### 1. Set up the Database Environment with Docker

First, pull and run the Docker image to establish the PostgreSQL database environment.

```bash
# Pull the Docker image
docker pull arthurchien/operation_system_database

# Run the Docker container
docker run --rm -d -p 8080:5432 --name os_db -e POSTGRES_PASSWORD=mis arthurchien/operation_system_database
```

This will start a PostgreSQL server on port 8080 of your localhost. The `--rm` flag ensures that the container is removed after it stops, and `-d` runs the container in detached mode.

### 2. Activate the Python Virtual Environment

Before running the application, activate the Python virtual environment.

```bash
# Activate the virtual environment
source .venv/bin/activate
```

This command activates the virtual environment, which is necessary to install and run Python dependencies in an isolated environment.

### 3. Run the Flask Application

Finally, start the Flask application.

```bash
# Run the Flask application
flask run
```

This command starts the Flask server, allowing you to access the application locally.

---

Ensure that you follow these steps in sequence to properly set up and run the application. If you encounter any issues, verify that each command is executed in the correct directory and check for any error messages in the console.
