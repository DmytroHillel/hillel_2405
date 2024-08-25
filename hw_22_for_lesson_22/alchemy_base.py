from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# З'єднання з базою даних PostgreSQL
# Потрібно вказати правильні дані для вашої бази даних
DATABASE_URL = "postgresql://postgres:1234@localhost/postgres"
engine = create_engine(DATABASE_URL)

Base = declarative_base()
