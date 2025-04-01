from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os


DB = os.getenv('databasepatient')
DB_PORT = os.getenv('port')
DB_USER = os.getenv('username')
DB_PASSWORD = os.getenv('password')
DB_HOST = os.getenv('host')

URL_DATABASE = f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB}"

ssl_config = {"ssl": {"ssl": True}}
engine = create_engine(URL_DATABASE, connect_args=ssl_config)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def very():
    try:
        with engine.connect() as connection:
            return "Conectado"
    except Exception as e:
        return f"Ocurrió un error inesperado: {str(e)}"

