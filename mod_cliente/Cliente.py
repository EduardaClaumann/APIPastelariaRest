from pydantic import BaseModel


class Cliente(BaseModel):
    id_cliente: int = None
    nome: str
    cpf: str
    telefone: str = None
    dia_fiado: int
    compra_fiado: int
    senha: str = None