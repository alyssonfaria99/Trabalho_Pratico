import os, sys
from pathlib import Path


# funcao para ler os usuarios cadastrados e retornar um array de dicionarios contendo os 
# dados dos usuarios organizados
def ler_arquivo_txt(caminho_arquivo):
    dados = []
    with open(caminho_arquivo, 'r') as file:
        linhas = file.readlines()
        cabecalhos = [cabecalho.strip() for cabecalho in linhas[0].strip().split(',')]
        for linha in linhas[1:]:
            valores = linha.strip().split(',')
            registro = {cabecalhos[i]: valores[i].strip() for i in range(len(cabecalhos))}
            dados.append(registro)
    return dados


def criarUsuario():
    caminho_relativo = 'usuarios/usuarios.txt'
    caminho_absoluto = os.path.abspath(caminho_relativo)
    email = input('Email: ')

    # validando email único
    usuarios = open(caminho_absoluto,'r')
    linhas = usuarios.readlines()
    for linha in linhas:
        if email in linha:
            print('Email já cadastrado.')
            return
    usuarios.close()

    nome = input('Nome: ')
    nivel = input('Nível: ')
    id = input('Id único: ')
    senha = input('Senha: ')

    # adicionando o novo usuário no arquivo usuarios.txt
    usuariostxt = open(caminho_absoluto,'a')
    usuariostxt.write(f'{nome},{nivel},{id},{senha},{email}\n')
    usuariostxt.close()

def listarUsuarios():
    caminho_relativo = 'usuarios/usuarios.txt'
    caminho_absoluto = os.path.abspath(caminho_relativo)
    usuarios = ler_arquivo_txt(caminho_absoluto)
    for usuario in usuarios:
        print(f'Nome:{usuario['Nome']}, Nível: {usuario['Nivel']}')

def atualizarUsuario(email, id, nivel):
    novoNome = input('Novo nome: ')
    novaSenha = input('Nova senha: ')
    caminho_relativo = 'usuarios/usuarios.txt'
    caminho_absoluto = os.path.abspath(caminho_relativo)

    # excluindo o usuario
    usuariostxt = open(caminho_absoluto, 'r')
    linhas = usuariostxt.readlines()
    cabecalhos = linhas[0]
    linhasAtualizadas = [cabecalhos]
    for linha in linhas[1:]:
        if email not in linha:
            linhasAtualizadas.append(linha)
    usuariostxt.close()
    escreverTxt = open(caminho_absoluto,'w')
    escreverTxt.writelines(linhasAtualizadas)

    # adicionando o usuario com as informações atualizadas
    escreverTxt.writelines(f'{novoNome},{nivel},{id},{novaSenha},{email}\n')
    escreverTxt.close()
    return

def excluirUsuario(email):
    caminho_relativo = 'usuarios/usuarios.txt'
    caminho_absoluto = os.path.abspath(caminho_relativo)
    usuariostxt = open(caminho_absoluto, 'r')
    linhas = usuariostxt.readlines()
    cabecalhos = linhas[0]
    linhasAtualizadas = [cabecalhos]
    for linha in linhas[1:]:
        if email not in linha:
            linhasAtualizadas.append(linha)
    usuariostxt.close()
    escreverTxt = open(caminho_absoluto,'w')
    escreverTxt.writelines(linhasAtualizadas)
    escreverTxt.close()
    return


