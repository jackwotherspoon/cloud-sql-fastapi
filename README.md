# cloud-sql-fastapi
A sample web application built using [FastAPI](https://fastapi.tiangolo.com/) connected to Cloud SQL (via the [Cloud SQL Python Connector](https://github.com/GoogleCloudPlatform/cloud-sql-python-connector)).

## Before you begin
1. Create a Cloud SQL Instance by following these 
[instructions](https://cloud.google.com/sql/docs/postgres/create-instance). 

Note the connection string, database user, and database password that you create.

2. Create a database for your application by following these 
[instructions](https://cloud.google.com/sql/docs/postgres/create-manage-databases). 

Note the database name. 

3. Create a service account with the 'Cloud SQL Client' IAM role by following these 
[instructions](https://cloud.google.com/sql/docs/postgres/connect-external-app#4_if_required_by_your_authentication_method_create_a_service_account).

Download the JSON key for the service account to authenticate your connection.

## Running locally
To run this application locally on your machine:

1. Clone the repository using Git and change directories
```sh
git clone https://github.com/jackwotherspoon/cloud-sql-fastapi.git
cd cloud-sql-fastapi
```

2. Install the dependencies
```sh
pip install -r requirements.txt
```

3. Fill in the `.env` file with your Cloud SQL specific values and path to service account JSON key.
```
INSTANCE_CONNECTION_NAME="project-id:region:instance-name"
DB_USER="my-db-user"
DB_PASS="my-db-pass"
DB_NAME="my-database"
GOOGLE_APPLICATION_CREDENTIALS="path/to/keys.json"
```

4. Run the application
```sh
uvicorn app.main:app --reload
```

The application is now running locally! Point your web browser at http://127.0.0.1:8000/ to view it.

**Note:** Remember to remove the `--reload` when not in a development environment.
It helps a lot during development, but you shouldn't use it in production.

## Deploy to Cloud Run
The application can be deployed to [Cloud Run](https://cloud.google.com/run) through the following steps:

1. Build the container image
```sh
gcloud builds submit --tag gcr.io/[YOUR_PROJECT_ID]/cloud-sql-fastapi
```

2. Deploy the service to Cloud Run
Replace environment variables with the correct values for your Cloud SQL
instance configuration as well as service account email of previously created service account.
```sh
gcloud run deploy cloud-sql-fastapi --image gcr.io/<PROJECT_ID>/cloud-sql-fastapi \
  --service-account='<SERVICE_ACCOUNT_EMAIL>' \
  --set-env-vars INSTANCE_CONNECTION_NAME='<PROJECT-ID>:<INSTANCE-REGION>:<INSTANCE-NAME>' \
  --set-env-vars DB_USER='<YOUR_DB_USER_NAME>' \
  --set-env-vars DB_PASS='<YOUR_DB_PASSWORD>' \
  --set-env-vars DB_NAME='<YOUR_DB_NAME>'
```

Take note of the URL output at the end of the deployment process.
This is the endpoint for your FastAPI application!
