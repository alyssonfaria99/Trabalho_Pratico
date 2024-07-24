from login import realizarLogin
from usuarios.usuarios import criarUsuario, listarUsuarios, atualizarUsuario, excluirUsuario
from produtos.produtos import listarPorCodigo, adicionarProduto, excluirProduto, atualizarProduto, listarPorNomes,listarPorPrecos
from pathlib import Path
import os

cadastrado = input(' 1 - Login\n 2 - Cadastre-se\n')
if cadastrado == '1':
    logado = realizarLogin()
    while logado == False:
        logado = realizarLogin()
    if logado['nivel'] == 'Gerente':
        print(' 1 - Listar Usuários\n 2 - Atualizar Usuário\n 3 - Excluir Usuário\n 4 - Buscar produto por código\n 5 - Adicionar Produto\n 6 - Excluir Produto\n 7 - Atualizar Produto\n 8 - Listar por Nomes\n 9 - Listar por Preço')
        acao = input('Escolha uma opção:')
        if acao == '1':
            listarUsuarios()
        if acao == '2':
            atualizarUsuario(email=logado['email'],id=logado['id'],nivel=logado['nivel'])
        if acao == '3':
            excluirUsuario(email=logado['email'])
        if acao == '4':
            listarPorCodigo()
        if acao == '5':
            adicionarProduto()
        if acao == '6':
            excluirProduto()
        if acao == '7':
            atualizarProduto()
        if acao == '8':
            listarPorNomes()
        if acao == '9':
            listarPorPrecos()


    if logado['nivel'] == 'Funcionario':
        print(' 1 - Listar Usuários\n 2 - Buscar produto por código\n 3 - Adicionar Produto\n 4 - Atualizar Produto\n 5 - Listar por Nomes\n 6 - Listar por Preço')
        acao = input('Escolha uma opção:')
        if acao == '1':
            listarUsuarios()
        if acao == '2':
            listarPorCodigo()
        if acao == '3':
            adicionarProduto()
        if acao == '4':
            atualizarProduto()
        if acao == '5':
            listarPorNomes()
        if acao == '6':
            listarPorPrecos()

if cadastrado == '2':
    criarUsuario()




