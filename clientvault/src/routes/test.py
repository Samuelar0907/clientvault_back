from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from src.database.database import Base
from src.database.models import Test
from ..database.crud import ClientService

a = ClientService ()
router = APIRouter(prefix="/test", tags=["prueba"])

@router.post("/test/")
def create_test(name: str, age: int):
    a.add_a (name, age)

    return "Agregado correctamente "
    

# Endpoint para obtener todos los registros de la tabla test
@router.get("/test/")
def get_tests(db: Session = Depends(Base)):
    tests = db.query(Test).all()  # Consultar todos los registros
    return tests

# Endpoint para obtener un registro por su ID
@router.get("/test/{test_id}")
def get_test(test_id: int, db: Session = Depends(Base)):
    db_test = db.query(Test).filter(Test.id == test_id).first()  # Consultar por ID
    if db_test is None:
        return {"message": "Registro no encontrado"}
    return db_test