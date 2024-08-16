# My FastAPI Project

## Overview

This project is a FastAPI application that:

1. Accepts a user-uploaded CSV file containing company information.
2. Parses the CSV file, extracts column names, and creates a new column called "Technology Company" using a classification API.
3. Connects to a PostgreSQL database and creates a new table with the extracted columns and the additional column.

## Project Structure

- `main.py`: Contains the FastAPI application and endpoints.
- `utils.py`: Includes utility functions for LLM API integration.
- `db.py`: Manages database interaction using SQLAlchemy.
- `Dockerfile`: Provides Docker setup for the project.
- `.env`: Defines environment variables.
- `pyproject.toml`: Manages dependencies using Poetry.
- `poetry.lock`: Lock file for Poetry dependencies.

## Getting Started

### Prerequisites

1. **Python**: Ensure you have Python 3.11 installed.
2. **Poetry**: Install Poetry for dependency management.

   ```bash
   pip install poetry
Install Dependencies
Clone the repository and install the dependencies using Poetry:

 ```bash
git clone <repository-url>
cd my_fastapi_project
poetry install

```
### Run the Application
Start the FastAPI application using Uvicorn:

```
poetry run uvicorn main:app --reload
```
The application will be accessible at :
```
http://127.0.0.1:8000
```

### Build and Run Docker Container
To build and run the Docker container, follow these steps:

Build Docker Image:

```
docker build -t my_fastapi_project .
```
### Run Docker Container:

```
docker run -p 8000:8000 --env-file .env my_fastapi_project

```
Ensure that you have a .env file in the project directory with the required environment variables.


API Endpoint

```
POST /uploadcsv/
```

Upload a CSV file with a Description column. The server will process the file, add a new column called "Technology Company", and create a new table in the database.

Example Request
http
```
POST /uploadcsv/
```
Content-Type: multipart/form-data

--boundary
Content-Disposition: form-data; name="file"; filename="example.csv"
Content-Type: text/csv

<CSV content>
--boundary--
Example Response
json

```
{
  "columns": ["column1", "column2", "Description", "Technology Company"],
  "message": "CSV processed and table created"
}
```
### Environment Variables

Set the following environment variables in your .env file:

DATABASE_URL: The URL for connecting to the PostgreSQL database 

```postgresql://postgres:password@localhost/db```.

API_KEY: API key for the LLM classification service.

## License

This project is licensed under the MIT License.
