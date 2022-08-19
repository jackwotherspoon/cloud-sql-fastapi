import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from google.cloud.sql.connector import Connector, IPTypes

# load env vars
load_dotenv()

# Cloud SQL Python Connector creator function
def getconn():
    # if env var PRIVATE_IP is set to True, use private IP Cloud SQL connections
    ip_type = IPTypes.PRIVATE if os.getenv("PRIVATE_IP") == True else IPTypes.PUBLIC
    # initialize Cloud SQL Python connector object
    with Connector(ip_type=ip_type) as connector:
        conn = connector.connect(
            os.getenv('INSTANCE_CONNECTION_NAME'),
            "pg8000",
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASS"),
            db=os.getenv("DB_NAME")
        )
        return conn

SQLALCHEMY_DATABASE_URL = "postgresql+pg8000://"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, creator=getconn
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
