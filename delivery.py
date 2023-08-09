from typing import Union
from pydantic import BaseModel
from fastapi import FastAPI

app = FastAPI()
class Pedido(BaseModel):
    qtde_prod: str
    descricao_prod: str
    codigo_prod: str
    endereco: str
    forma_pgto: str
    telefone: str
    nome_cliente: str
    


@app.post("/criar_pedido")

def fazer_pedido(pedido: Pedido):
    return {"msg": "World"}

@app.put("/cancelar_pedido")
def cancelar_pedido(numero: int):
    return {"msg": "pedido cancelado"}

@app.get("/listar_pedido")
def listar_pedido():
    return {"msg": "pedidos"}

@app.put("/aceitar_pedido")
def aceitar_pedido(numero: int):
    return {"msg": "pedido confirmado"}

@app.put("/rejeitar_pedido")
def rejeitar_pedido(numero: int):
    return {"msg": "pedido rejeitado"}







