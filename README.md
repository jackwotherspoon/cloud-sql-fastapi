# cloud-sql-fastapi
A sample web application built using [FastAPI](https://fastapi.tiangolo.com/) connected to Cloud SQL (via the [Cloud SQL Python Connector](https://github.com/GoogleCloudPlatform/cloud-sql-python-connector)).

## Deploy to Cloud Run
The application can be deployed to [Cloud Run](https://cloud.google.com/run) through the following steps:

1. Build the container image:
```sh
gcloud builds submit --tag gcr.io/[YOUR_PROJECT_ID]/cloud-sql-fastapi
```

2. Deploy the service to Cloud Run:
```sh
gcloud run deploy cloud-sql-fastapi --image gcr.io/<PROJECT_ID>/cloud-sql-fastapi \
  --set-env-vars INSTANCE_CONNECTION_NAME='<PROJECT-ID>:<INSTANCE-REGION>:<INSTANCE-NAME>' \
  --set-env-vars DB_USER='<YOUR_DB_USER_NAME>' \
  --set-env-vars DB_PASS='<YOUR_DB_PASSWORD>' \
  --set-env-vars DB_NAME='<YOUR_DB_NAME>'
```

Take note of the URL output at the end of the deployment process.
This is the endpoint for your FastAPI application!

Replace environment variables with the correct values for your Cloud SQL
instance configuration.
