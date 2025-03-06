



from ..database.crud import ClientService
from ..models.client import Client
from ..models.fono import Telefono
from ..models.direccion import Direcciones



class Handlerclient ():
    
    crud = ClientService ()    
    def add_handler_client (self,client : Client, direccion: Direcciones, fono: Telefono )->str:
        try:
            direccion_id_data = self.crud.add_direccion(direccion)
            telefono_id_data = self.crud.add_tel(fono)
            
     
            client.direccion_id = direccion_id_data
            client.telefono_id = telefono_id_data
           
            response = self.crud.add_client (client)
            return response
        except Exception as e :
            print("Error adding client: ", e)

    def handler_get_comuna (self):
        try:
            response  =self.crud.get_comuna ()
            return response
        except Exception as e :
            print("Error adding client: ", e)

