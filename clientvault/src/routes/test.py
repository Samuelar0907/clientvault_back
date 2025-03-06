from datetime import date

from ..models.client import Client
from fastapi import APIRouter
from ..database.crud import ClientService
from ..controllers.client_handler import Handlerclient
from ..models.fono import Telefono
from ..models.direccion import Direcciones

Crud = ClientService ()
handler = Handlerclient ()
router = APIRouter(prefix="/test", tags=["prueba"])

@router.post("/AddClient")
def create_test(id_paciente : str,
                 pnombre :str,
                 snombre:str,
                 appaterno:str,
                 apmaterno:str,
                 pais_id :int,
                 identificacion_id : int,
                 num_identificacion :str,

                 f_reg_alma :date,
                 f_nac : date,
                 genero :str,
                 prevision_id :int,
                 ocupacion_id :int,
                 celular : str,
                 
                 direccion: str,
                 descripcion : str,
                 comuna_id : int,
                 sucursal_id :int,
                                  
                 academico_id :int,
                 mail_princ : str,
                 mail_sec :str,
                 ult_visita :date,
                 tel_fijo : str= None,
                 familiar : str=None

                 ):
    
    try:
        paciente = Client(
            id_paciente,
            pnombre,
            snombre,
            appaterno,
            apmaterno,
            pais_id,
            num_identificacion,
            identificacion_id,
            academico_id,
            f_reg_alma,
            f_nac,
            genero,
            prevision_id,
            ocupacion_id,
            celular,
            tel_fijo,
            familiar,
            direccion,
            descripcion,
            comuna_id,
            sucursal_id,
            mail_princ,
            mail_sec,
            ult_visita
        
            
        )
        direccion_obj = Direcciones(direccion=direccion, descripcion=descripcion, comuna_id=comuna_id)
        telefono_obj = Telefono(celular=celular, tel_fijo=tel_fijo, familiar=familiar)

    
        handler.add_handler_client(paciente,direccion_obj,telefono_obj)
        return "Client added successfully"
    except Exception as e :
        return f"Ocurrió un error inesperado: {str(e)}"
    

    
    
@router.get ("/get")
def dasdaa ():
    try:
        response = handler.handler_get_comuna ()
        return response
    except Exception as e :
      return f"Ocurrió un error inesperado: {str(e)}"
