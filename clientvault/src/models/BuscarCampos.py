from typing import Optional
from pydantic import BaseModel

class BuscarCampos(BaseModel):
    id_paciente: Optional[int]
    pnombre: Optional[str]
    snombre: Optional[str]
    appaterno: Optional[str]
    apmaterno: Optional[str]
    mail_princ: Optional[str]
    identificacion_id: Optional[int]
    num_identificacion: Optional[str]
