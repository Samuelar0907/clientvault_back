

from ..models.clientP import ClientPotencial
from ..database.database import SessionLocal


class ClienPotentialService:
    def __init__(self):
        self.db = SessionLocal()

    def add_client_potential (self,clientp : ClientPotencial ):
        try:
            print(clientp.__dict__)
            paciente = ClientPotencial(**vars(clientp))
            self.db.add(paciente)
            self.db.commit()
            self.db.refresh(paciente)
            return "registrado exitosamente"
        except Exception as e:
            self.db.rollback()  
            raise e  
        finally:
            self.db.close()


    
