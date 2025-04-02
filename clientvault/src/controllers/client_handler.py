from src.models.BuscarCampos import BuscarCampos
from ..database.crud import ClientService
from ..models.client import Client
from ..models.fono import Telefono
from ..models.direccion import Direcciones



class Handlerclient():
    
    crud = ClientService()
    def add_handler_client(self,client : Client, direccion: Direcciones, fono: Telefono )->str:
        try:
        # if self.crud.get_num_identificacion(client.num_identificacion):
        #     print("ya exsiste el documento\n")
        #     return "el paciente ya esta registrado, verifique que el rut, dni o pasaporte sea correcto"
        # else:
            direccion_id_data = self.crud.add_direccion(direccion)
            telefono_id_data = self.crud.add_tel(fono)
            # if client.identificacion_id == 2 or client.identificacion_id == 3: 
            #     isonum = self.crud.get_pais_iso(client.pais_id)
            #     id_pacient_iso = client.id_paciente+ str(isonum)
            #     client.id_paciente = id_pacient_iso
            print("\nagregar paciente\n\n")
            client.direccion_id = direccion_id_data
            client.telefono_id = telefono_id_data
            response = self.crud.add_client(client)
            return response
        except Exception as e :
            print("Error adding client: ", e)

    def edit_handler_client(self, client: Client, direccion: Direcciones, fono: Telefono, id_paciente: int) -> str:
        try:
            # Editar dirección usando el ID del paciente
            direccion_id_data = self.crud.edit_direccion(direccion, id_paciente)
            
            # Editar teléfono usando el ID del paciente
            telefono_id_data = self.crud.edit_fono(fono, id_paciente)
            
            # Actualizar las referencias en el cliente
            client.direccion_id = direccion_id_data
            client.telefono_id = telefono_id_data
            
            # Editar el cliente principal
            response = self.crud.edit_client(client)
            
            return response
        except Exception as e:
            print(f"Error editando cliente {id_paciente}: {e}")
            raise e



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

    def handler_get_client (self):
        try:
            search = self.crud.get_clients()
            patient_list = self.__format(search)
            return patient_list
        except Exception as e:
            print("Error when i try to get all client: ", str(e))
  
    def handler_get_client_search (self, buscar: BuscarCampos):
        try:
            search = self.crud.get_clients_search(buscar)
            print(search)
            patient_list = self.__format(search)
            return patient_list
        except Exception as e:
            print("Error when searching for patients: ", str(e))
  
    def __format(self, search: list):
        try:
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