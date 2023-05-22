from fastapi import FastAPI, Depends, HTTPException, Body
from sqlalchemy.orm import Session
from exceptions import UsuarioException, UPAException, AnamneseException
from database import get_db, engine
from auth.auth_handler import signJWT
from auth.auth_bearer import JWTBearer
import crud, models, schemas

models.Base.metadata.create_all(bind=engine)
app = FastAPI()

# signup
@app.post("/api/signup", tags=["usuario"])
async def create_usuario_signup(usuario: schemas.UsuarioCreate = Body(...), db: Session = Depends(get_db)):
    try:
        crud.create_usuario(db, usuario)
        return signJWT(usuario.email)
    except UsuarioException as cie:
        raise HTTPException(**cie.__dict__)

# login
@app.post("/api/login", tags=["usuario"])
async def user_login(usuario: schemas.UsuarioLoginSchema = Body(...), db: Session = Depends(get_db)):
    if crud.check_usuario(db, usuario):
        return signJWT(usuario.email)
    raise HTTPException(status_code=400, detail="USUARIO_INCORRETO")

# usuário
@app.get("/api/usuarios/{usuario_id}", dependencies=[Depends(JWTBearer())], response_model=schemas.Usuario)
def get_usuario_by_id(usuario_id: int, db: Session = Depends(get_db)):
    try:
        return crud.get_usuario_by_id(db, usuario_id)
    except UsuarioException as cie:
        raise HTTPException(**cie.__dict__)

@app.get("/api/usuarios", dependencies=[Depends(JWTBearer())], response_model=schemas.PaginatedUsuario)
def get_all_usuarios(db: Session = Depends(get_db), offset: int = 0, limit: int = 10):
    db_usuarios = crud.get_all_usuarios(db, offset, limit)
    response = {"limit": limit, "offset": offset, "data": db_usuarios}
    return response

@app.post("/api/usuarios", dependencies=[Depends(JWTBearer())], response_model=schemas.Usuario)
def create_usuario(usuario: schemas.UsuarioCreate, db: Session = Depends(get_db)):
    try:
        return crud.create_usuario(db, usuario)
    except UsuarioException as cie:
        raise HTTPException(**cie.__dict__)

@app.put("/api/usuarios/{usuario_id}", dependencies=[Depends(JWTBearer())], response_model=schemas.Usuario)
def update_usuario(usuario_id: int, usuario: schemas.UsuarioCreate, db: Session = Depends(get_db)):
    try:
        return crud.update_usuario(db, usuario_id, usuario)
    except UsuarioException as cie:
        raise HTTPException(**cie.__dict__)

@app.delete("/api/usuarios/{usuario_id}", dependencies=[Depends(JWTBearer())])
def delete_usuario_by_id(usuario_id: int, db: Session = Depends(get_db)):
    try:
        return crud.delete_usuario_by_id(db, usuario_id)
    except UsuarioException as cie:
        raise HTTPException(**cie.__dict__)

# UPA
@app.get("/api/upas/{upa_id}", dependencies=[Depends(JWTBearer())], response_model=schemas.UPA)
def get_upa_by_id(upa_id: int, db: Session = Depends(get_db)):
    try:
        return crud.get_upa_by_id(db, upa_id)
    except UPAException as cie:
        raise HTTPException(**cie.__dict__)

@app.get("/api/upas", dependencies=[Depends(JWTBearer())], response_model=schemas.PaginatedUPA)
def get_all_upas(db: Session = Depends(get_db), offset: int = 0, limit: int = 10):
    db_upas = crud.get_all_upas(db, offset, limit)
    response = {"limit": limit, "offset": offset, "data": db_upas}
    return response

@app.post("/api/upas", dependencies=[Depends(JWTBearer())], response_model=schemas.UPA)
def create_upa(upa: schemas.UPACreate, db: Session = Depends(get_db)):
    try:
        return crud.create_upa(db, upa)
    except UPAException as cie:
        raise HTTPException(**cie.__dict__)

@app.put("/api/upas/{upa_id}", dependencies=[Depends(JWTBearer())], response_model=schemas.UPA)
def update_upa(upa_id: int, upa: schemas.UPACreate, db: Session = Depends(get_db)):
    try:
        return crud.update_upa(db, upa_id, upa)
    except UPAException as cie:
        raise HTTPException(**cie.__dict__)

@app.delete("/api/upas/{upa_id}", dependencies=[Depends(JWTBearer())])
def delete_upa_by_id(upa_id: int, db: Session = Depends(get_db)):
    try:
        return crud.delete_upa_by_id(db, upa_id)
    except UPAException as cie:
        raise HTTPException(**cie.__dict__)

# Anamnese
@app.post("/api/anamneses", dependencies=[Depends(JWTBearer())], response_model=schemas.Anamnese)
def create_anamnese(anamnese: schemas.AnamneseCreate, db: Session = Depends(get_db)):
    try:
        return crud.create_anamnese(db, anamnese)
    except AnamneseException as cie:
        raise HTTPException(**cie.__dict__)

@app.get("/api/anamneses/{anamnese_id}", dependencies=[Depends(JWTBearer())], response_model=schemas.Anamnese)
def get_anamnese_by_id(anamnese_id: int, db: Session = Depends(get_db)):
    try:
        return crud.get_anamnese_by_id(db, anamnese_id)
    except AnamneseException as cie:
        raise HTTPException(**cie.__dict__)
    
@app.get("/api/anamneses", dependencies=[Depends(JWTBearer())], response_model=schemas.PaginatedAnamnese)
def get_all_anamneses(db: Session = Depends(get_db), offset: int = 0, limit: int = 10):
    db_anamneses = crud.get_all_anamneses(db, offset, limit)
    response = {"limit": limit, "offset": offset, "data": db_anamneses}
    return response
    
@app.put("/api/anamneses/{anamnese_id}", dependencies=[Depends(JWTBearer())], response_model=schemas.Anamnese)
def update_anamnese(anamnese_id: int, anamnese: schemas.AnamneseCreate, db: Session = Depends(get_db)):
    return crud.update_anamnese(db, anamnese_id, anamnese)
    
@app.delete("/api/anamneses/{anamnese_id}", dependencies=[Depends(JWTBearer())])
def delete_anamnese_by_id(anamnese_id: int, db: Session = Depends(get_db)):
    try:
        return crud.delete_anamnese_by_id(db, anamnese_id)
    except AnamneseException as cie:
        raise HTTPException(**cie.__dict__)
