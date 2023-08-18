import sqlite3
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

def fazer_pedido(p: Pedido):
    try:
        c= sqlite3.connect('/Users/Ijovem01/yongalien/database/vendas.db')
        cr = c.cursor()
        cr.execute("""  INSERT INTO pedido (qtde_prod, descricao_prod, codigo_prod, endereco, forma_pgto, telefone, nome, status) VALUES (?,?,?,?,?,?,?,?) """, (p.qtde_prod, p.descricao_prod, p.codigo_prod, p.endereco, p.forma_pgto, p.telefone, p.nome_cliente,1))
        c.commit()
        c.close()
    except:
        return {"mensagem": "erro ao gravar o pedido"}
    else:
        return{"mensagem": "pedido salvo com sucesso"}

@app.put("/cancelar_pedido")
def cancelar_pedido(numero: int):
    try:
        c= sqlite3.connect('/Users/Ijovem01/yongalien/database/vendas.db')
        cr = c.cursor()
        cr.execute("update pedido set status=0 where id = ?", (numero,))
        c.commit()
        c.close()
    except:
        return {"mensagem": "erro ao cancelar o pedido"}
    else:
        return{"mensagem": "pedido cancelado com sucesso"}

@app.get("/listar_pedido")
def listar_pedido():
    try:
        c= sqlite3.connect('/Users/Ijovem01/yongalien/database/vendas.db')
        cr = c.cursor()
        cr.execute("""  SELECT * FROM  pedido """)
        lista= cr.fetchall()
        c.close()
        return lista
    except:
        return {"mensagem": "sem pedidos"}


@app.put("/aceitar_pedido")
def aceitar_pedido(numero: int):
    try:
        c= sqlite3.connect('/Users/Ijovem01/yongalien/database/vendas.db')
        cr = c.cursor()
        cr.execute("update pedido set status=2 where id = ?", (numero,))
        c.commit()
        c.close()
    except:
        return {"mensagem": "erro ao cancelar o pedido"}
    else:
        return{"mensagem": "pedido cancelado com sucesso"}

@app.put("/rejeitar_pedido")
def rejeitar_pedido(numero: int):
    try:
        c= sqlite3.connect('/Users/Ijovem01/yongalien/database/vendas.db')
        cr = c.cursor()
        cr.execute("update pedido set status=3 where id = ?", (numero,))
        c.commit()
        c.close()
    except:
        return {"mensagem": "erro ao cancelar o pedido"}
    else:
        return{"mensagem": "pedido cancelado com sucesso"}

@app.get("/listar_feito")
def listar_feito():
    try:
        c= sqlite3.connect('/Users/Ijovem01/yongalien/database/vendas.db')
        cr = c.cursor()
        cr.execute("""  SELECT * FROM  pedido where status = 1 """)
        lista= cr.fetchall()
        c.close()
        return lista
    except:
        return {"mensagem": "sem pedidos"}

@app.get("/listar_aceito")
def listar_aceito():
    try:
        c= sqlite3.connect('/Users/Ijovem01/yongalien/database/vendas.db')
        cr = c.cursor()
        cr.execute("""  SELECT * FROM  pedido where status = 2 """)
        lista= cr.fetchall()
        c.close()
        return lista
    except:
        return {"mensagem": "sem pedidos"}

@app.get("/listar_cancelado")
def listar_cancelado():
    try:
        c= sqlite3.connect('/Users/Ijovem01/yongalien/database/vendas.db')
        cr = c.cursor()
        cr.execute("""  SELECT * FROM  pedido where status = 0 """)
        lista= cr.fetchall()
        c.close()
        return lista
    except:
        return {"mensagem": "sem pedidos"}

@app.get("/listar_rejeitado")
def listar_rejeitado():
    try:
        c= sqlite3.connect('/Users/Ijovem01/yongalien/database/vendas.db')
        cr = c.cursor()
        cr.execute("""  SELECT * FROM  pedido where status = 3 """)
        lista= cr.fetchall()
        c.close()
        return lista
    except:
        return {"mensagem": "sem pedidos"}








