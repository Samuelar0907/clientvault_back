from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os


# DB = os.getenv('MYSQL_DATABASE')  

# DB_PORT = os.getenv('MYSQL_PORT')  
# DB_USER = os.getenv('MYSQL_USER')  
# DB_PASSWORD = os.getenv('MYSQL_PASSWORD')  

# DB_HOST = os.getenv('MYSQL_HOST')  

# # URL de conexión a la base de datos MySQL

# URL_DATABASE = f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB}"
DB_USER = os.environ['POSTGRES_USER']
DB_PASSWORD = os.environ['POSTGRES_PASSWORD']
DB = os.environ['POSTGRES_DB']
DB_HOST = os.environ['POSTGRES_HOST']
DB_PORT = os.environ['POSTGRES_PORT'] 

URL_DATABASE = f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:6543/{DB}?sslmode=require"

engine = create_engine(URL_DATABASE)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def very():
    try:
        with engine.connect() as connection:
            return "Conectado"
    except Exception as e:
        return f"Ocurrió un error inesperado: {str(e)}"

