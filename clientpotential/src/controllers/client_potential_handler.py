from ..database.crud import ClienPotentialService
from ..models.clientP import clientPotencial




class HandlerClientPotential():
    
    crud = ClienPotentialService()
    
    def add_handler_client(self,clientp : clientPotencial )->str:
        try:
           response = self.crud.add_client_potential(clientp)
           
           return response
        except Exception as e :
            print("Error adding client: ", e)

    def get_clientPotential_handler (self):
        try:
            search = self.crud.get_clientPotential()
            patient_list = []
            for patient in search :
                patient_data=patient.__dict__.copy()
                relations = {
                    'cliente_status_id' : patient.cliente_status.tipo_cliente if patient.cliente_status else None
                 
                }
                patient_data.update(relations)
                remove = [
                    'cliente_status', 
                ]
                for key in remove:
                    patient_data.pop(key, None)
                patient_list.append(patient_data)
                
            return patient_list
        except Exception as e:
            print("Error when i try to get all client: ", str(e))