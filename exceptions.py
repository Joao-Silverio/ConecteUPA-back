class UsuarioException(Exception):
    ...

class UsuarioNotFoundError(UsuarioException):
    def __init__(self):
        self.status_code = 404
        self.detail = "USUARIO_NAO_ENCONTRADO"

class UsuarioAlreadyExistError(UsuarioException):
    def __init__(self):
        self.status_code = 409
        self.detail = "EMAIL_DUPLICADO"

class AnamneseException(Exception):
    ...

class AnamneseNotFoundError(AnamneseException):
    def __init__(self):
        self.status_code = 404
        self.detail = "ANAMNESE_NAO_ENCONTRADO"
        
class UPAException(Exception):
    ...

class UPANotFoundError(UPAException):
    def __init__(self):
        self.status_code = 404
        self.detail = "UPA_NAO_ENCONTRADO"