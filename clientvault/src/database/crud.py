from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from .database import get_db
from .models import Test  # Asegúrate de que el modelo esté importado correctamente

app = FastAPI()

# Endpoint para crear un nuevo registro en la tabla test
@app.post("/test/")
def create_test(name: str, age: int, db: Session = Depends(get_db)):
    db_test = Test(name=name, age=age)
    db.add(db_test)  # Agregar el nuevo registro a la sesión
    db.commit()  # Confirmar la transacción
    db.refresh(db_test)  # Recargar el objeto con los datos del DB
    return db_test

# Endpoint para obtener todos los registros de la tabla test
@app.get("/test/")
def get_tests(db: Session = Depends(get_db)):
    tests = db.query(Test).all()  # Consultar todos los registros
    return tests

# Endpoint para obtener un registro por su ID
@app.get("/test/{test_id}")
def get_test(test_id: int, db: Session = Depends(get_db)):
    db_test = db.query(Test).filter(Test.id == test_id).first()  # Consultar por ID
    if db_test is None:
        return {"message": "Registro no encontrado"}
    return db_test
