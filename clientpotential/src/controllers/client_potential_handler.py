from ..database.crud import ClienPotentialService
from ..models.clientP import ClientPotencial




class HandlerClientPotential():
    
    crud = ClienPotentialService()
    
    def add_handler_client(self,clientp : ClientPotencial )->str:
        try:
           response = self.crud.add_client_potential(clientp)
           
           return response
        except Exception as e :
            print("Error adding client: ", e)