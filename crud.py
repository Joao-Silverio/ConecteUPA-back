from sqlalchemy.orm import Session
from exceptions import UsuarioAlreadyExistError, UsuarioNotFoundError, UPANotFoundError, AnamneseNotFoundError
import bcrypt, models, schemas

#usuario
def check_usuario(db: Session, usuario: schemas.UsuarioLoginSchema):
    db_usuario = db.query(models.Usuario).filter(models.Usuario.email == usuario.email).first()
    if db_usuario is None:
        return False
    return bcrypt.checkpw(usuario.senha.encode('utf8'), db_usuario.senha.encode('utf8'))

def get_usuario_by_id(db: Session, usuario_id: int):
    db_usuario = db.query(models.Usuario).get(usuario_id)
    if db_usuario is None:
        raise UsuarioNotFoundError
    return db_usuario

def get_all_usuarios(db: Session, offset: int, limit: int):
    return db.query(models.Usuario).offset(offset).limit(limit).all()

def get_usuario_by_email(db: Session, usuario_email: str):
    return db.query(models.Usuario).filter(models.Usuario.email == usuario_email).first()

def get_usuario_by_nome(db: Session, usuario_nome: str):
    return db.query(models.Usuario).filter(models.Usuario.nome == usuario_nome).first()

def create_usuario(db: Session, usuario: schemas.UsuarioCreate):
    db_usuario = get_usuario_by_email(db, usuario.email)
    # O parâmetro rounds do gensalt determina a complexidade. O padrão é 12.
    usuario.senha = bcrypt.hashpw(usuario.senha.encode('utf8'), bcrypt.gensalt())
    if db_usuario is not None:
        raise UsuarioAlreadyExistError
    db_usuario = models.Usuario(**usuario.dict())
    db.add(db_usuario)
    db.commit()
    db.refresh(db_usuario)
    return db_usuario

def update_usuario(db: Session, usuario_id: int, usuario: schemas.UsuarioCreate):
    db_usuario = get_usuario_by_id(db, usuario_id)
    db_usuario.nome = usuario.nome
    db_usuario.email = usuario.email
    db_usuario.historico = usuario.historico
    if usuario.senha != "":
        # O parâmetro rounds do gensalt determina a complexidade. O padrão é 12.
        db_usuario.senha = bcrypt.hashpw(usuario.senha.encode('utf8'), bcrypt.gensalt())
    db.commit()
    db.refresh(db_usuario)
    return db_usuario

def delete_usuario_by_id(db: Session, usuario_id: int):
    db_usuario = get_usuario_by_id(db, usuario_id)
    db.delete(db_usuario)
    db.commit()
    return

#upas
def get_upa_by_id(db: Session, upa_id: int):
    db_upa = db.query(models.UPA).get(upa_id)
    if db_upa is None:
        raise UPANotFoundError
    return db_upa

def get_all_upas(db: Session, offset: int, limit: int):
    return db.query(models.UPA).offset(offset).limit(limit).all()

def create_upa(db: Session, upa: schemas.UPACreate):
    db_upa = models.UPA(**upa.dict())
    db.add(db_upa)
    db.commit()
    db.refresh(db_upa)
    return db_upa

def update_upa(db: Session, upa_id: int, upa: schemas.UPACreate):
    db_upa = get_upa_by_id(db, upa_id)
    db_upa.nome = upa.nome
    db_upa.lugar = upa.lugar
    db_upa.telefone = upa.telefone
    db.commit()
    db.refresh(db_upa)
    return db_upa

def delete_upa_by_id(db: Session, upa_id: int):
    db_upa = get_upa_by_id(db, upa_id)
    db.delete(db_upa)
    db.commit()
    return

#anamnese
def create_anamnese(db: Session, anamnese: schemas.AnamneseCreate):
    get_usuario_by_id(db, anamnese.id_usuario)
    db_anamnese = models.Anamnese(id_usuario=anamnese.id_usuario, data=anamnese.data)
    db.add(db_anamnese)
    db.commit()
    db.refresh(db_anamnese)
    return db_anamnese

def get_anamnese_by_id(db: Session, anamnese_id: int):
    db_anamnese = db.query(models.Anamnese).get(anamnese_id)
    if db_anamnese is None:
        raise AnamneseNotFoundError
    return db_anamnese

def get_all_anamneses(db: Session, offset: int, limit: int):
    return db.query(models.Anamnese).offset(offset).limit(limit).all()

def update_anamnese(db: Session, anamnese_id: int, anamnese: schemas.AnamneseUpdate):
    db_anamnese = get_anamnese_by_id(db, anamnese_id)
    db_anamnese.data = anamnese.data
    db.commit()
    db.refresh(db_anamnese)
    return db_anamnese

def delete_anamnese_by_id(db: Session, anamnese_id: int):
    db_anamnese = get_anamnese_by_id(db, anamnese_id)
    db.delete(db_anamnese)
    db.commit()
    return