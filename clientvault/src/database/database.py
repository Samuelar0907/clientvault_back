from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

# Obtener las variables de entorno
DB = os.getenv('MYSQL_DATABASE')  
DB_PORT = os.getenv('MYSQL_PORT')  
DB_USER = os.getenv('MYSQL_USER')  
DB_PASSWORD = os.getenv('MYSQL_PASSWORD')  
DB_HOST = os.getenv('MYSQL_HOST')  

# URL de conexión a la base de datos MySQL
URL_DATABASE = f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB}"

# Crear el motor de la base de datos
engine = create_engine(URL_DATABASE)

# Verificar la conexión e imprimir un mensaje si es exitosa
try:
    connection = engine.connect()
    print("✅ Conexión a la base de datos exitosa.")
    connection.close()
except Exception as e:
    print(f"❌ Error al conectar a la base de datos: {e}")

# Crear la sesión de SQLAlchemy
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Definir el tipo base para los modelos
Base = declarative_base()

# Función para obtener una sesión de la base de datos
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()