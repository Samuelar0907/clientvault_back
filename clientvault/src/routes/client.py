from datetime import date

from ..database.database import very

from ..models.client import Client
from fastapi import APIRouter
from ..database.crud import ClientService
from ..controllers.client_handler import Handlerclient
from ..models.fono import Telefono
from ..models.direccion import Direcciones

Crud = ClientService()
handler = Handlerclient()
router = APIRouter(prefix="/client", tags=["client"])

@router.get("/")
def test():
    return {"response": "World in testing for client"}

@router.post("/AddClient")
def create_test(id_paciente: str,
                 pnombre: str,
                 appaterno: str,
                 identificacion_id: int,
                 num_identificacion: str,
                 pais_id: int,

                 f_reg_alma: date,
                 f_nac: date,
                 genero: str,
                 prevision_id: int,
                 ocupacion_id: int,
                 celular: str,
                 
                 comuna_id: int,
                 direccion: str,
                 descripcion: str,
                 sucursal_id: int,
                                  
                 academico_id: int,
                 mail_princ: str,
                 ult_visita: date,
                 snombre: str= None,
                 apmaterno: str= None,
                 mail_sec: str= None,
                 tel_fijo: str= None,
                 familiar: str= None

                 ):
    
    try:
        paciente = Client(
            id_paciente=id_paciente,
            pnombre=pnombre,
            snombre=snombre,
            appaterno=appaterno,
            apmaterno=apmaterno,
            pais_id=pais_id,
            identificacion_id=identificacion_id,
            num_identificacion=num_identificacion,
            f_reg_alma=f_reg_alma,
            f_nac=f_nac,
            genero=genero,
            prevision_id=prevision_id,
            ocupacion_id=ocupacion_id,
            sucursal_id=sucursal_id,
            academico_id=academico_id,
            mail_princ=mail_princ,
            mail_sec=mail_sec,
            ult_visita=ult_visita
        )
        direccion_obj = Direcciones(direccion=direccion, descripcion=descripcion, comuna_id=comuna_id)
        telefono_obj = Telefono(celular=celular, tel_fijo=tel_fijo, familiar=familiar)

    
        response = handler.add_handler_client(paciente,direccion_obj,telefono_obj)
        return response
    except Exception as e:
        return f"Ocurrió un error inesperado: {str(e)}"
     
### gets ###
@router.get("/get/selects")
def json_selects():
    try:
        response = handler.handler_get_selects()
        return response
    except Exception as e:
      return f"Ocurrió un error inesperado: {str(e)}"

@router.get("/get/comuna/{id_region}")
def get_region(id_region: int):
    try:
        response = handler.handler_get_comuna(id_region)
        return response
    except Exception as e:
      return f"Ocurrió un error inesperado: {str(e)}"

@router.get("/get/ocupacion/{id_sector}")
def get_region(id_sector: int):
    try:
        response = handler.handler_get_ocupacion(id_sector)
        return response
    except Exception as e:
      return f"Ocurrió un error inesperado: {str(e)}"
    
@router.get("/get/pais/iso/{id_pais}")
def get_iso(id_pais: int):
    try:
        response = handler.handler_get_iso(id_pais)
        return response
    except Exception as e:
      return f"Ocurrió un error inesperado: {str(e)}"
    
@router.get("/getClient")
def get_patient():
    try:
        response = handler.handler_get_client()
        return response
    except Exception as e:
      return f"Ocurrió un error inesperado: {str(e)}"
    
# GET PRA VERIFICAR CONECCION A DB

@router.get("/testDB")
def get_very_db():
    try:
        response = very ()
        return response
    except Exception as e:
      return f"Ocurrió un error inesperado: {str(e)}"
