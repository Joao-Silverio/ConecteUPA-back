from datetime import date
from typing import List  
from pydantic import BaseModel

class UsuarioBase(BaseModel):
    nome: str
    email: str
class UsuarioCreate(UsuarioBase):
    senha: str
class Usuario(UsuarioBase):
    id: int
    class Config:
        orm_mode = True
class UsuarioLoginSchema(BaseModel):
    email: str
    senha: str
    class Config:
        schema_extra = {
            "example": {
                "email": "x@x.com",
                "senha": "pass"
            }
        }
class PaginatedUsuario(BaseModel):
    limit: int
    offset: int
    data: List[Usuario]

#Cadastro anamnese
class AnamneseBase(BaseModel):
    id_usuario: int
    data: date
    resumo: str
class AnamneseUpdate(BaseModel):
    pass 
class AnamneseCreate(AnamneseBase):
    pass
class Anamnese(AnamneseBase):
    id: int
    usuario: Usuario = {}
    class Config:
        orm_mode = True
class PaginatedAnamnese(BaseModel):
    limit: int
    offset: int
    data: List[Anamnese]

#cadastro upas
class UPABase(BaseModel):
    nome: str
    lugar: str
    telefone: str
class UPACreate(UPABase):
    pass
class UPA(UPABase):
    id: int
    class Config:
        orm_mode = True
class UPALoginSchema(BaseModel):
    email: str
    senha: str
    class Config:
        schema_extra = {
            "example": {
                "email": "x@x.com",
                "senha": "pass"
            }
        }
class PaginatedUPA(BaseModel):
    limit: int
    offset: int
    data: List[UPA]