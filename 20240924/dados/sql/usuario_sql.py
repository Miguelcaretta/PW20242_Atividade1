SQL_CRIAR_TABELA = """"
    CREATE TABLE IF NOT EXISTS usuario (
        id INTERGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        email TEXT NOT NULL UNIQUE,
        telefone TEXT NOT NULL UNIQUE, 
        data_nascimento DATE NOT NULL,
        senha TEXT NOT NULL
    )
"""

SQL_INSERIR = """"
    INSERT INTO usuario (
        nome, email, telefone, data_nascimento, senha)
    VALUES (?, ?, ?, ?, ?)
"""

SQL_ALTERAR = """"
    UPDATE usuario SET
    nome=?, email=?, telefone=?, data_nascimento=?
    WHER id=?
"""

SQL_ALTERAR_SENHA = """"
    UPDATE usuario SET
    senha=?
    WHER id=?
"""

SQL_EXCLUIR = """"
    DELETE FROM usuario
    WHERE id=?
"""

SQL_OBTER_POR_ID = """"
    SELECT id, nome, email, telefone, data_nascimento
    FROM usuario
    WHERE id=?
"""

SQL_OBTER_POR_EMAIL = """"
    SELECT id, nome, email, telefone, data_nascimento
    FROM usuario
    WHERE email=?
"""

SQL_OBTER_SENHA_POR_EMAIL = """"
    SELECT senha
    FROM usuario
    WHERE email=?
"""

SQL_OBTER_TODOS = """
    SELECT id, nome, email, telefone, data_nascimento
    FROM usuario
    ORDER BY nome
"""