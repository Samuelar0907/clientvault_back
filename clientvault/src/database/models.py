from sqlalchemy import Column, Date, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from .database import Base
import os

TABLE_COMUNA = os.getenv("TABLE_COMUNA")
TABLE_DIRECCION = os.getenv("TABLE_DIRECCION")
TABLE_IDENTIFICACION = os.getenv("TABLE_IDENTIFICACION")
TABLE_OCUPACION = os.getenv("TABLE_OCUPACION")
TABLE_PACIENTE = os.getenv("TABLE_PACIENTE")
TABLE_PAIS = os.getenv("TABLE_PAIS")
TABLE_PREVISION = os.getenv("TABLE_PREVISION")
TABLE_REGION = os.getenv("TABLE_REGION")
TABLE_SECTOR = os.getenv("TABLE_SECTOR")
TABLE_SUCURSAL = os.getenv("TABLE_SUCURSAL")
TABLE_TELEFONOS = os.getenv("TABLE_TELEFONOS")
TABLE_NVACADEMICO = os.getenv("TABLE_NVACADEMICO")


class Region(Base):
    __tablename__ = TABLE_REGION

    id_region = Column(Integer, primary_key=True, autoincrement=True)
    n_region = Column(String(100), nullable=False)
    comunas = relationship("Comuna", back_populates="region")

class User(Base):
    __tablename__ = "users"
    id_user = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String, index=True)
    password = Column(String)


class Comuna(Base):
    __tablename__ = TABLE_COMUNA

    id_comuna = Column(Integer, primary_key=True, autoincrement=True)
    n_comuna = Column(String(100), nullable=False)
    region_id = Column(Integer, ForeignKey(f"{TABLE_REGION}.id_region"), nullable=False)
    region = relationship("Region", back_populates="comunas")
    direcciones = relationship("Direccion", back_populates="comuna")


class Direccion(Base):
    __tablename__ = TABLE_DIRECCION

    id_direccion = Column(Integer, primary_key=True, autoincrement=True)
    direccion = Column(String(200), nullable=False)
    descripcion = Column(String(1000), nullable= True)
    comuna_id = Column(Integer, ForeignKey(f"{TABLE_COMUNA}.id_comuna"), nullable=False)
    comuna = relationship("Comuna", back_populates="direcciones")
    pacientes = relationship("Paciente", back_populates="direccion")


class Identificacion(Base):
    __tablename__ = TABLE_IDENTIFICACION

    id_identificacion = Column(Integer, primary_key=True, autoincrement=True)
    n_documeto = Column(String(30))
    pacientes = relationship("Paciente", back_populates="identificacion")

class Academico(Base):
    __tablename__ = TABLE_NVACADEMICO

    id_academiconv = Column(Integer, primary_key=True, autoincrement=True)
    n_academiconv = Column(String(100), nullable=False)
    pacientes = relationship("Paciente", back_populates="nivel_academico")



class Sector(Base):
    __tablename__ = TABLE_SECTOR

    id_sector = Column(Integer, primary_key=True, autoincrement=True)
    tipo_sector = Column(String(100), nullable=False)
    ocupaciones = relationship("Ocupacion", back_populates="sector")


class Ocupacion(Base):
    __tablename__ = TABLE_OCUPACION

    id_ocupacion = Column(Integer, primary_key=True, autoincrement=True)
    sector_id = Column(Integer, ForeignKey(f"{TABLE_SECTOR}.id_sector"), nullable=False)
    tipo_ocupacion = Column(String(75), nullable=False)
    sector = relationship("Sector", back_populates="ocupaciones")
    pacientes = relationship("Paciente", back_populates="ocupacion")


class Pais(Base):
    __tablename__ = TABLE_PAIS

    id_pais = Column(Integer, primary_key=True, autoincrement=True)
    iso = Column(String(2))
    isonum = Column(Integer)
    nombre = Column(String(80))
    pacientes = relationship("Paciente", back_populates="pais")


class Prevision(Base):
    __tablename__ = TABLE_PREVISION

    id_prevision = Column(Integer, primary_key=True, autoincrement=True)
    tipo_prev = Column(String(100), nullable=False)
    pacientes = relationship("Paciente", back_populates="prevision")


class Sucursal(Base):
    __tablename__ = TABLE_SUCURSAL

    id_sucursal = Column(Integer, primary_key=True, autoincrement=True)
    sucursal = Column(String(100), nullable=False)
    pacientes = relationship("Paciente", back_populates="sucursal")


class Telefonos(Base):
    __tablename__ = TABLE_TELEFONOS

    id_telefonos = Column(Integer, primary_key=True, autoincrement=True)
    celular = Column(String(15), nullable=False)
    tel_fijo = Column(String(15), nullable=True)
    familiar = Column(String(15), nullable=True)
    pacientes = relationship("Paciente", back_populates="telefono")



class Paciente(Base):
    __tablename__ = TABLE_PACIENTE

    id_paciente = Column(String(25), primary_key=True, index=True)
    pnombre = Column(String(50), nullable=False)
    snombre = Column(String(100), nullable=True)
    appaterno = Column(String(100), nullable=False)
    apmaterno = Column(String(100), nullable= True)
    pais_id = Column(Integer, ForeignKey(f"{TABLE_PAIS}.id_pais"), nullable=False)
    
    identificacion_id = Column(
        Integer, ForeignKey(f"{TABLE_IDENTIFICACION}.id_identificacion"), nullable=False
    )
    num_identificacion = Column(String(20))
   
    f_reg_alma = Column(Date, nullable=False)
    f_nac = Column(Date, nullable=False)
    genero = Column(String(10), nullable=False)
    prevision_id = Column(Integer, ForeignKey(f"{TABLE_PREVISION}.id_prevision"), nullable=False)
    ocupacion_id = Column(Integer, ForeignKey(f"{TABLE_OCUPACION}.id_ocupacion"), nullable=False)
    telefono_id = Column(
        Integer, ForeignKey(f"{TABLE_TELEFONOS}.id_telefonos"), nullable=False
    )
    direccion_id = Column(
        Integer, ForeignKey(f"{TABLE_DIRECCION}.id_direccion"), nullable=False
    )
    sucursal_id = Column(Integer, ForeignKey(f"{TABLE_SUCURSAL}.id_sucursal"), nullable=False)
    academico_id = Column(
        Integer, ForeignKey(f"{TABLE_NVACADEMICO}.id_academiconv"), nullable=False
    )
    mail_princ = Column(String(255), nullable=False)
    mail_sec = Column(String(255), nullable=True)
    ult_visita = Column(Date, nullable=False)

    pais = relationship("Pais", back_populates="pacientes")
    identificacion = relationship("Identificacion", back_populates="pacientes")
    nivel_academico = relationship("Academico", back_populates="pacientes")
    prevision = relationship("Prevision", back_populates="pacientes")
    ocupacion = relationship("Ocupacion", back_populates="pacientes")
    telefono = relationship("Telefonos", back_populates="pacientes")
    direccion = relationship("Direccion", back_populates="pacientes")
    sucursal = relationship("Sucursal", back_populates="pacientes")
