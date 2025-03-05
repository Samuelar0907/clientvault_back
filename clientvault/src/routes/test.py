from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from src.database.database import get_db
from src.database.models import Test

router = APIRouter(prefix="/test", tags=["prueba"])

@router.post("/test/")
def create_test(name: str, age: int, db: Session = Depends(get_db)):
    db_test = Test(name=name, age=age)
    db.add(db_test)  # Agregar el nuevo registro a la sesión
    db.commit()  # Confirmar la transacción
    db.refresh(db_test)  # Recargar el objeto con los datos del DB
    return db_test

# Endpoint para obtener todos los registros de la tabla test
@router.get("/test/")
def get_tests(db: Session = Depends(get_db)):
    tests = db.query(Test).all()  # Consultar todos los registros
    return tests

# Endpoint para obtener un registro por su ID
@router.get("/test/{test_id}")
def get_test(test_id: int, db: Session = Depends(get_db)):
    db_test = db.query(Test).filter(Test.id == test_id).first()  # Consultar por ID
    if db_test is None:
        return {"message": "Registro no encontrado"}
    return db_test