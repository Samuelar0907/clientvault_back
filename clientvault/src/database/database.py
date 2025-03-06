from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

DB = os.getenv('MYSQL_DATABASE')  
DB_PORT = os.getenv('MYSQL_PORT')  
DB_USER = os.getenv('MYSQL_USER')  
DB_PASSWORD = os.getenv('MYSQL_PASSWORD')  
DB_HOST = os.getenv('MYSQL_HOST')


URL_DATABASE = f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB}"

engine = create_engine(URL_DATABASE)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def very():
    try:
        with engine.connect() as connection:
            return "Conectado"
    except Exception as e:
        return f"Ocurrió un error inesperado: {str(e)}"

