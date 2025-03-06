



from .database import SessionLocal
from ..database.models import Test


class ClientService ():

    db = SessionLocal()

    def add_a(self, name: str, age: int):
        nuevo_registro = Test(name=name, age=age)
        self.db.add(nuevo_registro)
        self.db.commit()
        self.db.refresh(nuevo_registro)
        return nuevo_registro