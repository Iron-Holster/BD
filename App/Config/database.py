from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from contextlib import contextmanager

# Definindo parâmetros para acesso de banco de dados

db_user = "aluno"
db_password = "aluno_senha"
db_name = "meu_banco_senai"
db_host = "localhost"
db_port = "3306"

# Endereço (URL) para conexão com banco de dados

DATABASE_URL = f"mysql+pymysql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"

#Criando banco de dados

db = create_engine(DATABASE_URL)

# Criando conexão com banco de dados.

Session = sessionmaker(bind=db)
session = Session()

#gerenciando conexão com banco de dados.
@contextmanager
def get_db():
    db = Session()
    try:
        yield db # Realiza tentativa de operação no BD.
        db.commit #Salvando no BD
    except Exception as erro:
        db.rollback() # Caso ocorra algum erro, desfaz alterações no BD
        raise erro # Caso ocorra algum erro, mostra mensagem de erro no terminal
    finally:
        db.close() # fecha conexão com BD.