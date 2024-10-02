from typing import Optional
from sql.usuario_sql import *
from templates.sql.models.usuario_model import Usuario
from util import obter_conexao


def criar_tabela():
    with obter_conexao() as conexao:
        db = conexao.cursor()
        db.execute(SQL_CRIAR_TABELA)

def inserir(usuario: Usuario) -> Optional[Usuario]
    with obter_conexao() as conexao:
        db = conexao.cursor()
        db.execute(SQL_INSERIR, 
            (usuario.nome,
            usuario.email,
            usuario.telefone,
            usuario.data_nascimento,
            usuario.senha))
        if db.rowcount > 0: 
            usuario.id = db.lastrowid
            return usuario
        else:
            return None
        
def criar_tabela():
    with obter_conexao() as conexao:
        db = conexao.cursor()
        db.execute(SQL_CRIAR_TABELA)
        tuplas = db.execute(sql_obter_todos).fectchal
        usuarios = [usuario(*t) for t in tuplas]
        return usuarios
