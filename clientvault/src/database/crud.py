import uuid
from .database import SessionLocal
from sqlalchemy.orm import  joinedload
from ..models.client import Client
from ..database.models import (
Ocupacion, Paciente,
Direccion, Pais,
Sector, Telefonos,
Comuna, Region,
Identificacion, Academico,
Prevision, Sucursal,
User
)
from ..models.direccion import Direcciones
from ..models.fono import Telefono


class ClientService:
    def __init__(self):
        self.db = SessionLocal()

### agregaciones ###
    def add_direccion(self, direc: Direcciones):
        try:
            address = Direccion(**vars(direc))
            self.db.add(address)
            self.db.commit()
            self.db.refresh(address)
            return address.id_direccion
        except Exception as e:
            self.db.rollback()  
            raise e  
        finally:
            self.db.close()

    def add_tel(self, fono: Telefono):
        try:
            fonos_data = Telefonos(**vars(fono))
            self.db.add(fonos_data)
            self.db.commit()
            self.db.refresh(fonos_data)
            return fonos_data.id_telefonos
        except Exception as e:
            self.db.rollback()  
            raise e  
        finally:
            self.db.close()

    def add_client(self, client: Client) -> int:
        try:
            print(client.__dict__)
            paciente = Paciente(
                **vars(client),
                uid=str(uuid.uuid4()))
            self.db.add(paciente)
            self.db.commit()
            self.db.refresh(paciente)
            return "registrado exitosamente"
        except Exception as e:
            self.db.rollback()  
            raise e  
        finally:
            self.db.close()
    #otros
    def edit_direccion(self, direc: Direcciones, id: int):
        try:
            if id is None:
                raise ValueError("El valor de id_direccion no puede ser None")

            direccion = self.db.query(Direccion).filter_by(id_direccion=id).first()
            if direccion is None:
                raise ValueError(f"No se encontro la direccion con el id {id}")

            direccion_data_dict = vars(direc)

            for key, value in direccion_data_dict.items():
                if key == 'id_direccion':
                    continue
                setattr(direccion, key, value)

            self.db.commit()
            self.db.refresh(direccion)
            return direccion.id_direccion
        except Exception as e:
            self.db.rollback()
            raise e
        finally:
            self.db.close()

    def edit_fono(self, fonos: Telefonos, id: int):
        try:
            if id is None:
                raise ValueError("El valor de id_telefonos no puede ser None")

            # Buscar el teléfono existente
            telefono = self.db.query(Telefonos).filter_by(id_telefonos=id).first()
            if telefono is None:
                raise ValueError(f"No se encontro el telefono con el id {id}")

            telefono_data_dict = vars(fonos)

            for key, value in telefono_data_dict.items():
                if key == 'id_telefonos':
                    continue
                setattr(telefono, key, value)

            self.db.commit()
            self.db.refresh(telefono)
            return telefono.id_telefonos
        except Exception as e:
            self.db.rollback()
            raise e
        finally:
            self.db.close()

    def edit_client(self, client: Client) -> str:
        try:
            paciente = self.db.query(Paciente).filter_by(id_paciente=client.id_paciente).first()

            if paciente is None:
                raise ValueError(f"No se encontró el Paciente con ID {client.id_paciente}")

            current_telefono_id = paciente.telefono_id
            current_direccion_id = paciente.direccion_id
            current_uid = paciente.uid  
            client_data_dict = vars(client)

            for key, value in client_data_dict.items():
                if key == "uid" and value is None: 
                    continue
                setattr(paciente, key, value)

            paciente.telefono_id = client.telefono_id if client.telefono_id is not None else current_telefono_id
            paciente.direccion_id = client.direccion_id if client.direccion_id is not None else current_direccion_id
            paciente.uid = client.uid if client.uid is not None else current_uid  

            self.db.commit()
            self.db.refresh(paciente)
            return "actualizado exitosamente"
        except Exception as e:
            self.db.rollback()
            raise e
        finally:
            self.db.close()

    ### gets ###
    def get_pais(self):
        try:
            response = self.db.query(Pais).order_by(Pais.nombre).all()
            return response
        except Exception as e:
            self.db.rollback()  
            raise e  
        finally:
            self.db.close()

    def get_tipo_documento(self):
        try:
            response = self.db.query(Identificacion).order_by(Identificacion.n_documeto).all()
            return response
        except Exception as e:
            self.db.rollback()  
            raise e  
        finally:
            self.db.close()

    def get_nivel_academico(self):
        try:
            response = self.db.query(Academico).order_by(Academico.id_academiconv).all()
            return response
        except Exception as e:
            self.db.rollback()  
            raise e  
        finally:
            self.db.close()

    def get_prevision(self):
        try:
            response = self.db.query(Prevision).order_by(Prevision.tipo_prev).all()
            return response
        except Exception as e:
            self.db.rollback()  
            raise e  
        finally:
            self.db.close()

    def get_sucursal(self):
        try:
            response = self.db.query(Sucursal).order_by(Sucursal.sucursal).all()
            return response
        except Exception as e:
            self.db.rollback()  
            raise e  
        finally:
            self.db.close()

    def get_region(self):
        try:
            response = self.db.query(Region).order_by(Region.n_region).all()
            return response
        except Exception as e:
            self.db.rollback()  
            raise e  
        finally:
            self.db.close()

    def get_sector(self):
        try:
            response = self.db.query(Sector).order_by(Sector.tipo_sector).all()
            return response
        except Exception as e:
            self.db.rollback()  
            raise e  
        finally:
            self.db.close()

### gets con parametros ###
    def get_num_identificacion(self, num_identificacion):
        try:
            paciente = self.db.query(Paciente).filter(Paciente.num_identificacion == num_identificacion).first()
            
            if paciente is None:
                return None
            else:
                return True
            
        except Exception as e:
            self.db.rollback()
            raise e
        finally:
            self.db.close()

    def get_ocupacion(self, id_sector):
        try:
            response = self.db.query(Ocupacion).filter(Ocupacion.sector_id == id_sector).order_by(Ocupacion.tipo_ocupacion).all()
            return response
        except Exception as e:
            self.db.rollback()  
            raise e  
        finally:
            self.db.close()
    

    def get_comuna(self, id_region):
        try:
            response = self.db.query(Comuna).filter(Comuna.region_id == id_region).order_by(Comuna.n_comuna).all()
            return response
        except Exception as e:
            self.db.rollback()  
            raise e  
        finally:
            self.db.close()

    def get_pais_iso(self, id_pais):
        try:
            response = self.db.query(Pais).filter(Pais.id_pais == id_pais).one()
            return response.isonum
        except Exception as e:
            self.db.rollback()  
            raise e  
        finally:
            self.db.close()

    def get_clients (self):
        try:
            client_search = (
                self.db.query(Paciente).options(
                    joinedload(Paciente.pais),
                    joinedload(Paciente.identificacion),
                    joinedload(Paciente.nivel_academico),
                    joinedload(Paciente.prevision),
                    joinedload(Paciente.ocupacion),
                    joinedload(Paciente.telefono),
                    joinedload(Paciente.direccion),
                    joinedload(Paciente.sucursal),
                ).all()
            )
            for client in client_search:
                client.uid = str(uuid.UUID(bytes=client.uid))

            return client_search
        except Exception as e:
            return f"error{str(e)}"
        



class AuthService:
    def __init__(self):
        self.db = SessionLocal()
    
    def authenticate_user(self, email: str, password: str):
        try:
            user = self.db.query(User).filter(
                User.email == email,
                User.password == password
            ).first()
            return user
        except Exception as e:
            raise e
        finally:
            self.db.close()

    
