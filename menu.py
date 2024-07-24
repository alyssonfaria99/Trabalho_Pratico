from usuarios.usuarios import listarUsuarios, atualizarUsuario, excluirUsuario
from produtos.produtos import listarPorCodigo, adicionarProduto, excluirProduto, atualizarProduto, listarPorNomes,listarPorPrecos

def irParaMenu(logado):
# realiza a operacao solicitada pelo usuario e volta para o menu em seguida
    if logado['nivel'] == 'Gerente':
        print(' 1 - Listar Usuários\n 2 - Atualizar Usuário\n 3 - Excluir Usuário\n 4 - Buscar produto por código\n 5 - Adicionar Produto\n 6 - Excluir Produto\n 7 - Atualizar Produto\n 8 - Listar por Nomes\n 9 - Listar por Preço\n 10 - Sair')
        acao = input('Escolha uma opção:')
        if acao == '1':
            listarUsuarios()
            irParaMenu(logado)
        if acao == '2':
            atualizarUsuario(email=logado['email'],id=logado['id'],nivel=logado['nivel'])
            irParaMenu(logado)
        if acao == '3':
            excluirUsuario()
            irParaMenu(logado)
        if acao == '4':
            listarPorCodigo()
            irParaMenu(logado)
        if acao == '5':
            adicionarProduto()
            irParaMenu(logado)
        if acao == '6':
            excluirProduto()
            irParaMenu(logado)
        if acao == '7':
            atualizarProduto()
            irParaMenu(logado)
        if acao == '8':
            listarPorNomes()
            irParaMenu(logado)
        if acao == '9':
            listarPorPrecos()
            irParaMenu(logado)
        if acao == '10':
            print('Logout realizado.')
            return

    if logado['nivel'] == 'Funcionario':
        print(' 1 - Listar Usuários\n 2 - Buscar produto por código\n 3 - Adicionar Produto\n 4 - Atualizar Produto\n 5 - Listar por Nomes\n 6 - Listar por Preço\n 7 - Sair')
        acao = input('Escolha uma opção:')
        if acao == '1':
            listarUsuarios()
            irParaMenu(logado)
        if acao == '2':
            listarPorCodigo()
            irParaMenu(logado)
        if acao == '3':
            adicionarProduto()
            irParaMenu(logado)
        if acao == '4':
            atualizarProduto()
            irParaMenu(logado)
        if acao == '5':
            listarPorNomes()
            irParaMenu(logado)
        if acao == '6':
            listarPorPrecos()
            irParaMenu(logado)
        if acao == '7':
            print('Logout realizado.')
            return