from sqlalchemy import Column, Date, ForeignKey, Integer, String, Text
from sqlalchemy.orm import relationship
from .database import Base
import os

TABLE_POTENTIAL_CLIENT = os.getenv("TABLE_POTENTIAL_CLIENT")
TABLE_CLIENTSTATUS = os.getenv("TABLE_CLIENTSTATUS")

class ClienteStatus(Base):
    __tablename__ = TABLE_CLIENTSTATUS

    id_status = Column(Integer, primary_key=True, autoincrement=True)
    tipo_cliente = Column(String(50))

    # Relación con PotentialClient
    potential_clients = relationship("PotentialClient", back_populates="cliente_status")

class PotentialClient(Base):
    __tablename__ = TABLE_POTENTIAL_CLIENT

    id = Column(Integer, primary_key=True, index=True)
    pnombre = Column(String(50), nullable=False)
    snombre = Column(String(50), nullable=True)
    appaterno = Column(String(50), nullable=False)
    apmaterno = Column(String(50), nullable=True)
    email = Column(String(100), index=False)
    numero_telefono = Column(String(20), index=False)
    razon_contacto = Column(Text())
    cliente_status_id = Column(
        Integer, ForeignKey(f"{TABLE_CLIENTSTATUS}.id_status"), nullable=False
    )
    fecha_creacion = Column(Date, index=False)

    # Relación con ClienteStatus
    cliente_status = relationship("ClienteStatus", back_populates="potential_clients")
