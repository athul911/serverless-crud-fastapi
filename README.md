# serverless-crud-fastapi
Serverless CRUD Application with Python, Pynamodb, and Separated Logic

This project implements a serverless CRUD (Create, Read, Update, Delete) application using Python, Pynamodb for interacting with DynamoDB, and separates the logic into models, routers, and services.

Features:

    Implements CRUD operations for items stored in a DynamoDB table.
    Uses Pynamodb for simplified interaction with DynamoDB.
    Separates logic into models, routers, and services for better organization and maintainability.
    Uses FastAPI for defining API endpoints.

Requirements:

    Python 3.9
    AWS account with DynamoDB access
    boto3 (installed automatically by serverless-python-requirements)
    pynamodb (specified in requirements.txt)
    fastapi (specified in requirements.txt)

Setup:

    Clone this repository.
    Configure your AWS credentials (e.g., through ~/.aws/config).
    Install dependencies:

pip install -r requirements.txt

Deployment:

    Deploy the application to AWS using Serverless Framework:

serverless deploy

API Endpoints:

    Create Item:
        Method: POST
        URL: /api/items
        Body: JSON object with id and data properties

    Get Item:
        Method: GET
        URL: /api/items/{id}
        Path parameter: id of the item

    Update Item:
        Method: PUT
        URL: /api/items/{id}
        Path parameter: id of the item
        Body: JSON object with properties to update

    Delete Item:
        Method: DELETE
        URL: /api/items/{id}
        Path parameter: id of the item
