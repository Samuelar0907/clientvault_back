

from ..models.clientP import clientPotencial
from ..database.models import PotentialClient
from ..database.database import SessionLocal
from sqlalchemy.orm import  joinedload
from ..models.DateObject import DateObject

class ClienPotentialService:
    def __init__(self):
        self.db = SessionLocal()

    def add_client_potential (self,clientp : clientPotencial ):
        try:
            new_seeds = PotentialClient (
                fecha_creacion = DateObject.get_now_date(self)
            )
            paciente_data_dict = vars(clientp)
            for key, value in paciente_data_dict.items():
                if key in ["fecha_creacion"] and getattr(new_seeds, key) is not None:
                    continue
                setattr(new_seeds, key, value)

        
           
            self.db.add(new_seeds)
            self.db.commit()
            self.db.refresh(new_seeds)
            return "resgistrado correctamente"
        except Exception as e:
            self.db.rollback()  
            raise e  
        finally:
            self.db.close()

    #get

    def get_clientPotential (self):
        try:
            search = (self.db.query(PotentialClient).options(
                joinedload(PotentialClient.cliente_status),
                ).all()
            )

            return search
        except Exception as e :
            return f"error{str(e)}"
