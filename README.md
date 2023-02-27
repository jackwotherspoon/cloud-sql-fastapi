# cloud-sql-fastapi
Sample web applications built using [FastAPI](https://fastapi.tiangolo.com/) that integrate Google's Cloud SQL databases (via the [Cloud SQL Python Connector](https://github.com/GoogleCloudPlatform/cloud-sql-python-connector)).

## :bar_chart: :computer: Tabs vs Spaces (Beginner, [README](tabs-vs-spaces/README.md))

A voting web application that aims to settle the age old programming debate, should you use Tabs or Spaces?

<p align="center">
    <img src="https://raw.githubusercontent.com/jackwotherspoon/cloud-sql-fastapi/main/docs/images/tabs-vs-spaces.png" alt="tabs-vs-spaces application">
</p>

This tutorial is great for beginners and includes the following:
- Integrates a Cloud SQL database with FastAPI ([Cloud SQL Python Connector](https://github.com/GoogleCloudPlatform/cloud-sql-python-connector) + [SQLAlchemy](https://www.sqlalchemy.org/))
- FastAPI application database best practices (`database.py`, `models.py`, `schemas.py`)
- Rendering a simple HTML template and sending __Form__ data

To implement this web application proceed to the [Tabs vs Spaces README](tabs-vs-spaces/README.md)

## :chart_with_upwards_trend: :moneybag: Expense Tracker (Intermediate, [README](expense-tracker/README.md))

A backend application that implements CRUD operations for tracking expenses stored in Cloud SQL.

<p align="center">
    <img src="https://raw.githubusercontent.com/jackwotherspoon/cloud-sql-fastapi/main/docs/images/expense-tracker.png" alt="expense-tracker application">
</p>

This tutorial is great for developers looking to build a backend application with CRUD APIs that leverage Cloud SQL:
- Integrates a Cloud SQL database with FastAPI ([Cloud SQL Python Connector](https://github.com/GoogleCloudPlatform/cloud-sql-python-connector) + [SQLAlchemy](https://www.sqlalchemy.org/))
- FastAPI application database best practices (`database.py`, `models.py`, `schemas.py`)
- Create, Read, Update, Delete (CRUD) APIs connecting to database
- Basic error handling

To implement this web application proceed to the [Expense Tracker README](expense-tracker/README.md)
