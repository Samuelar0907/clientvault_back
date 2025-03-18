from ..database.crud import ClientService
from ..models.client import Client
from ..models.fono import Telefono
from ..models.direccion import Direcciones



class Handlerclient():
    
    crud = ClientService()
    def add_handler_client(self,client : Client, direccion: Direcciones, fono: Telefono )->str:
        try:
            if self.crud.get_num_identificacion(client.num_identificacion):
                print("ya exsiste el documento\n")
                return "el docuemnto ya esta registrado"
            else:
                direccion_id_data = self.crud.add_direccion(direccion)
                telefono_id_data = self.crud.add_tel(fono)
                

                client.direccion_id = direccion_id_data
                client.telefono_id = telefono_id_data
            
                response = self.crud.add_client(client)
                return response
        except Exception as e :
            print("Error adding client: ", e)

    def handler_get_selects(self):
        try:
            data_pais = self.crud.get_pais()
            data_documento = self.crud.get_tipo_documento()
            data_prevision = self.crud.get_prevision()
            data_sector = self.crud.get_sector()
            data_region = self.crud.get_region()
            data_sucursal = self.crud.get_sucursal()
            data_nivel_academico = self.crud.get_nivel_academico()

            select_options = {
                "pais": [{"value": item.id_pais, "label": item.nombre} for item in data_pais],
                "identificacion": [{"value": item.id_identificacion, "label": item.n_documeto} for item in data_documento],
                "prevision": [{"value": item.id_prevision, "label": item.tipo_prev} for item in data_prevision],
                "sector": [{"value": item.id_sector, "label": item.tipo_sector} for item in data_sector],
                "region": [{"value": item.id_region, "label": item.n_region} for item in data_region],
                "sucursal": [{"value": item.id_sucursal, "label": item.sucursal} for item in data_sucursal],
                "academico": [{"value": item.id_academiconv, "label": item.n_academiconv} for item in data_nivel_academico]
            }

            return select_options
        except Exception as e:
            print("Error al obtener los selects: ", e)
            return {"error": "Hubo un problema al obtener los selects"}


    def handler_get_comuna(self, id_region):
        try:
            response  =self.crud.get_comuna(id_region)
            return response
        except Exception as e :
            print("Error get comuna: ", e)

    def handler_get_ocupacion(self, id_sector):
        try:
            response  =self.crud.get_ocupacion(id_sector)
            return response
        except Exception as e :
            print("Error get ocupacion: ", e)
    
    def handler_get_iso(self, id_pais):
        try:
            response  =self.crud.get_pais_iso(id_pais)
            return response
        except Exception as e :
            print("Error get iso: ", e)

    def handler_get_client (self):
        try:
            search = self.crud.get_clients ()
            patient_list = []
            for patient in search :
                patient_data=patient.__dict__.copy()
                relations = {
                    'prevision_id' : patient.prevision.tipo_prev if patient.prevision else None,
                    'identificacion_id' : patient.identificacion.n_documeto if patient.identificacion else None,
                    'sucursal_id' : patient.sucursal.sucursal if patient.sucursal else None,
                    'academico_id' : patient.nivel_academico.n_academiconv if patient.nivel_academico else None,
                    'pais_id' : patient.pais.nombre if patient.pais else None
                }
                patient_data.update(relations)
                remove = [
                    'prevision',   'identificacion',
                    'sucursal', 'nivel_academico', 'pais',
                ]
                for key in remove:
                    patient_data.pop(key, None)
                patient_list.append(patient_data)
                
            return patient_list
        except Exception as e:
            print("Error when i try to get all client: ", str(e))
            


from ..database.crud import AuthService

class AuthHandler:
    crud = AuthService()
    def login_user(self, email: str, password: str):
        try:
            user = self.crud.authenticate_user(email, password)
            if not user:
                return {"success": False, "error": "Credenciales inválidas"}
            return {"success": True, "email": user.email}
        except Exception as e:
            return {"success": False, "error": str(e)}