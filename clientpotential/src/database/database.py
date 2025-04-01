from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os


DB = os.getenv('databaseclient')  
DB_PORT = os.getenv('port')  
DB_USER = os.getenv('username')  
DB_PASSWORD = os.getenv('password')  
DB_HOST = os.getenv('host')  
# SSLMODE = os.getenv("sslmode")

# URL de conexión a la base de datos MySQL

URL_DATABASE = f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB}"

ssl_config = {"ssl": {"ssl": True}}
engine = create_engine(URL_DATABASE, connect_args=ssl_config)
# DB_USER = os.environ['POSTGRES_USER2']
# DB_PASSWORD = os.environ['POSTGRES_PASSWORD2']
# DB = os.environ['POSTGRES_DB']
# DB_HOST = os.environ['POSTGRES_HOST2']
# DB_PORT = os.environ['POSTGRES_PORT'] 

# URL_DATABASE = f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:6543/{DB}?sslmode=require"

# engine = create_engine(URL_DATABASE)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def very():
    try:
        with engine.connect() as connection:
            return "Conectado"
    except Exception as e:
        return f"Ocurrió un error inesperado: {str(e)}"

