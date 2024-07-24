from login import realizarLogin
from usuarios.usuarios import criarUsuario
from menu import irParaMenu

cadastrado = input(' 1 - Login\n 2 - Cadastre-se\n')
if cadastrado == '1':
    logado = realizarLogin()
    while logado == False:
        logado = realizarLogin()
    irParaMenu(logado)

if cadastrado == '2':
    criarUsuario()
    print('Faça o login:')
    logado = realizarLogin()
    while logado == False:
        logado = realizarLogin()
    irParaMenu(logado)