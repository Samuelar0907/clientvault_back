from datetime import date

from ..database.database import very

from fastapi import APIRouter

from ..controllers.client_potential_handler import HandlerClientPotential

from ..models.clientP import clientPotencial

handler = HandlerClientPotential()
router = APIRouter(prefix="/clientPotential", tags=["clientPotential"])

@router.get("/")
def test():
    return {"response": "World in testing for clientPotential"}


@router.post("/addClientPotencial")
def add_clientPotencial(pnombre :str,
        appaterno:str,
        email:str,
        numero_telefono:str,
        razon_contacto:str,
        cliente_status_id:int,
     
        snombre: str= None,
        apmaterno: str= None):
    try:
        paciente = clientPotencial(
            
            pnombre=pnombre,
            snombre=snombre,
            appaterno=appaterno,
            email=email,
            numero_telefono=numero_telefono,
            razon_contacto=razon_contacto,
            cliente_status_id=cliente_status_id,
       
            apmaterno=apmaterno
        )
        response = handler.add_handler_client(paciente)
        return response
    except Exception as e:
      return f"Ocurrió un error inesperado: {str(e)}"

#get client potential

@router.get("/getclientPotential")
def get_potentialClient():
    try:
        response = handler.get_clientPotential_handler()
        return response
    except Exception as e:
      return f"Ocurrió un error inesperado: {str(e)}"

# GET PRA VERIFICAR CONECCION A DB

@router.get("/testDB")
def get_very2_db():
    try:
        response = very ()
        return response
    except Exception as e:
      return f"Ocurrió un error inesperado: {str(e)}"
