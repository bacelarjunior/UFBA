from fastapi import HTTPException, status


class CredenciaisInvalidasException(HTTPException):
    """
    Exceção para credenciais inválidas.
    """

    def __init__(self):
        super().__init__(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Credenciais inválidas",
            headers={"WWW-Authenticate": "Bearer"},
        )


class NaoAutorizadoException(HTTPException):
    """
    Exceção para nível de acesso inválido.
    """
    def _init_(self, detail="Não autorizado."):
        super()._init_(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=detail,
            headers={"WWW-Authenticate": "Bearer"},
        )
    