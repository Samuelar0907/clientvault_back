from sqlalchemy import Column, Integer, String
from ..database.database import Base
class Test(Base):
    __tablename__ = "test"  # El nombre de la tabla en la base de datos

    # Definir las columnas de la tabla
    id = Column(Integer, primary_key=True, index=True)  # Columna de id, clave primaria
    name = Column(String, index=True)  # Columna de nombre, índice
    age = Column(Integer)  # Columna de edad

    def __repr__(self):
        return f"<Test id={self.id} name={self.name} age={self.age}>"   


