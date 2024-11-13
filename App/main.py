from services.usuario_service import UsuarioService
from repositories.usuario_repository import UsuarioRepository
from config.database import Session
import os

session = Session()
repository  = UsuarioRepository(session)
service = UsuarioService(repository) 

#solicitando dados para o usuario
print("\nCadastrando usuario: ")
nome = input("Digite seu nome: ")
email = input("Digite seu email: ")
senha = input("Digite seu senha:")

service.criar_usuario(nome,email,senha)

#exibindo todos os registros na tabela "Usuarios" do banco de dados.
print("=== Listando usuários cadastrados ===")
lista_usuarios = service.listar_todos_usuarios()
for usuario in lista_usuarios:
    print(f"Nome: {usuario.nome} \nEmail: {usuario.email}")