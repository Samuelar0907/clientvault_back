


from .database import SessionLocal
from ..models.client import Client 
from ..database.models import Comuna
from ..database.models import Paciente,Direccion,Telefonos
from ..models.direccion import  Direcciones
from ..models.fono import Telefono


class ClientService ():

    db = SessionLocal()


    def add_direccion(self, direc:  Direcciones):
        try:
            address = Direccion(**vars(direc))  
            self.db.add(address)
            self.db.commit()
            self.db.refresh(address)
            return address.id_direccion
        finally:
            self.db.close()
    
    def add_direccion(self, direc:  Direcciones):
        try:
            address = Direccion(**vars(direc))  
            self.db.add(address)
            self.db.commit()
            self.db.refresh(address)
            return address.id_direccion
        finally:
            self.db.close()

    def add_direccion(self, direc:  Direcciones):
        try:
            address = Direccion(**vars(direc))  
            self.db.add(address)
            self.db.commit()
            self.db.refresh(address)
            return address.id_direccion
        finally:
            self.db.close()

    def add_tel(self, fono:  Telefono):
        try:
            fonos_data = Telefonos(**vars(fono))  
            self.db.add(fonos_data)
            self.db.commit()
            self.db.refresh(fonos_data)
            return fonos_data.id_telefonos
        finally:
            self.db.close()




    def add_client(self, client: Client) -> int:
        try:
            paciente = Paciente(**vars(client))  
            self.db.add(paciente)
            self.db.commit()
            self.db.refresh(paciente)
            return paciente
        finally:
            self.db.close()




    def get_comuna (self):
        open = self.db.query(Comuna).all()
        return open