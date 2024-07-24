from usuarios.usuarios import ler_arquivo_txt
from pathlib import Path


# a funcao solicita o email e a senha, verifica se coincidem com os que estao cadastrados
# se coincidir realiza o login e retorna um dicionario com os dados do usuario
def realizarLogin():
    caminho_arquivo = Path(__file__).parent / 'usuarios' / 'usuarios.txt'
    dados = ler_arquivo_txt(caminho_arquivo)
    login = input('Email:')
    senha = input('Senha:')

    for registro in dados:
        if registro['Email'] == login:
            if registro['Senha'] == senha:
                print('Login realizado com sucesso!')
                return {
                    'nivel': registro['Nivel'],
                    'email': registro['Email'],
                    'id': registro['Id']
                }
            else:
                print('Email ou senha incorretos')
                return False
    print('Email ou senha incorretos')
    return False



