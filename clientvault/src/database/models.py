
from sqlalchemy import Column, Date, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from .database import Base
import os

TABLE_COMUNA= os.getenv('TABLE_COMUNA')
TABLE_DIRECCION= os.getenv('TABLE_DIRECCION')
TABLE_IDENTIFICACION= os.getenv('TABLE_IDENTIFICACION')
TABLE_OCUPACION= os.getenv('TABLE_OCUPACION')
TABLE_PACIENTE= os.getenv('TABLE_PACIENTE')
TABLE_PAIS= os.getenv('TABLE_PAIS')
TABLE_PREVISION= os.getenv('TABLE_PREVISION')
TABLE_REGION= os.getenv('TABLE_REGION')
TABLE_SECTOR= os.getenv('TABLE_SECTOR')
TABLE_SUCURSAL= os.getenv('TABLE_SUCURSAL')
TABLE_TELEFONOS= os.getenv('TABLE_TELEFONOS')


class Region(Base):
    __tablename__ = 'region'
    id_region = Column(Integer, primary_key=True, autoincrement=True)
    n_region = Column(String(100), nullable=False)


class Comuna(Base): 
    __tablename__ = 'comuna'
    id_comuna = Column(Integer, primary_key=True, autoincrement=True)
    n_comuna = Column(String(100), nullable=False)
    region_id = Column(Integer, ForeignKey('region.id_region'), nullable=False)
    region = relationship("Region")

class Direccion(Base):
    __tablename__ = 'direccion'
    id_direccion = Column(Integer, primary_key=True, autoincrement=True)
    direccion = Column(String(200), nullable=False)
    descripcion = Column(String(1000))
    comuna_id = Column(Integer, ForeignKey('comuna.id_comuna'), nullable=False)
    comuna = relationship("Comuna")

class Identificacion(Base):
    __tablename__ = 'identificacion'
    id_identificacion = Column(Integer, primary_key=True, autoincrement=True)
    identificacion = Column(String(30),)

class Sector(Base):
    __tablename__ = 'sector'
    id_sector = Column(Integer, primary_key=True, autoincrement=True)
    tipo_sector = Column(String(100), nullable=False)

class Ocupacion(Base):
    __tablename__ = 'ocupacion'
    id_ocupacion = Column(Integer, primary_key=True, autoincrement=True)
    sector_id = Column(Integer, ForeignKey('sector.id_sector'), nullable=False)
    tipo_ocupacion = Column(String(75), nullable=False)
    sector = relationship("Sector")

class Pais(Base):
    __tablename__ = 'pais'
    id_pais = Column(Integer, primary_key=True, autoincrement=True)
    iso = Column(String(2))
    isonum = Column(Integer)
    nombre = Column(String(80))

class Prevision(Base):
    __tablename__ = 'prevision'
    id_prevision = Column(Integer, primary_key=True, autoincrement=True)
    tipo_prev = Column(String(100), nullable=False)

class Sucursal(Base):
    __tablename__ = 'sucursal'
    id_sucursal = Column(Integer, primary_key=True, autoincrement=True)
    sucursal = Column(String(100), nullable=False)

class Telefonos(Base):
    __tablename__ = 'telefonos'
    id_telefonos = Column(Integer, primary_key=True, autoincrement=True)
    celular = Column(String(15))
    tel_fijo = Column(String(15))
    familiar = Column(String(15))

class Academico(Base):
    __tablename__= 'nvacademico'
    id_academiconv = Column(Integer, primary_key=True, autoincrement=True)
    n_academiconv = Column(String(100), nullable=False)

class Paciente(Base):
    __tablename__ = 'paciente'
    id_paciente = Column(String(25), primary_key=True, index=True  )
    pnombre = Column(String(50), nullable=False)
    snombre = Column(String(100), nullable=False)
    ap_paterno = Column(String(100), nullable=False)
    apmaterno = Column(String(100))
    pais_id = Column(Integer, ForeignKey('pais.id_pais'), nullable=False)
    num_documento= Column(String(20))
    identificacion_id = Column(Integer, ForeignKey('identificacion.id_identificacion'), unique=True, nullable=False)
    f_reg_alma = Column(Date, nullable=False)
    f_nac = Column(Date, nullable=False)
    genero = Column(String(10), nullable=False)
    prevision_id = Column(Integer, ForeignKey('prevision.id_prevision'), nullable=False)
    ocupacion_id = Column(Integer, ForeignKey('ocupacion.id_ocupacion'), nullable=False)
    telefono_id = Column(Integer, ForeignKey('telefonos.id_telefonos'), unique=True, nullable=False)
    direccion_id = Column(Integer, ForeignKey('direccion.id_direccion'), unique=True, nullable=False)
    sucursal_id = Column(Integer, ForeignKey('sucursal.id_sucursal'), nullable=False)
    mail_princ = Column(String(255), nullable=False)
    mail_sec = Column(String(255))
    ult_visita = Column(Date)

    pais = relationship("Pais")
    identificacion = relationship("Identificacion")
    prevision = relationship("Prevision")
    ocupacion = relationship("Ocupacion")
    telefono = relationship("Telefonos")
    direccion = relationship("Direccion")
    sucursal = relationship("Sucursal")