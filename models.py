from sqlalchemy import Column, Integer, String, SmallInteger, Date, ForeignKey, Table
from sqlalchemy.orm import relationship
from database import Base

class Usuario(Base):
    __tablename__ = 'usuarios'
    
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(150))
    historico = Column(String(1000))
    email = Column(String(150), unique=True, index=True)
    senha = Column(String(255))
    anamnese = relationship("Anamnese", back_populates="usuario")

class Anamnese(Base):
    __tablename__ = 'anamneses'
    
    id = Column(Integer, primary_key=True, index=True)
    data = Column(Date)
    id_usuario = Column(Integer, ForeignKey("usuarios.id"), nullable=False)
    usuario = relationship("Usuario", back_populates="anamneses")

class UPA(Base):
    __tablename__ = 'upas'
    
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(150))
    lugar = Column(String(1000))
    telefone = Column(String(150))