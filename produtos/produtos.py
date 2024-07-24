import os

# funcao para ler os produtos cadastrados e retornar um array de dicionarios contendo os 
# dados dos produtos organizados
def ler_arquivo_produtos(caminho_arquivo):
    dados = []
    with open(caminho_arquivo, 'r') as file:
        linhas = file.readlines()
        cabecalhos = [cabecalho.strip() for cabecalho in linhas[0].strip().split(',')]
        for linha in linhas[1:]:
            valores = linha.strip().split(',')
            registro = {cabecalhos[i]: valores[i].strip() for i in range(len(cabecalhos))}
            dados.append(registro)
    return dados

def listarPorCodigo():
    caminho_relativo = 'produtos/produtos.txt'
    caminho_absoluto = os.path.abspath(caminho_relativo)
    produtos = ler_arquivo_produtos(caminho_absoluto)
    codigo = input('Código do produto: ')
    for produto in produtos:
        if codigo == produto['Codigo']:
            print(f'Produto: {produto['Nome']}, Preço: {produto['Preco']}, Estoque: {produto['Estoque']} ')
            return
    print('Produto não encontrado.')
    return 

def adicionarProduto():
    caminho_relativo = 'produtos/produtos.txt'
    caminho_absoluto = os.path.abspath(caminho_relativo)
    nome = input('Nome: ')
    codigo = input('Código: ')
    preco = input('Preço: ')
    quantidade = input('Quantidade: ')
    produtostxt = open(caminho_absoluto,'a')
    produtostxt.write(f'{nome},{codigo},{preco},{quantidade}\n')
    produtostxt.close()
    return

def excluirProduto():
    codigo = input('Código do produto a ser excluído: ')
    caminho_relativo = 'produtos/produtos.txt'
    caminho_absoluto = os.path.abspath(caminho_relativo)
    produtostxt = open(caminho_absoluto, 'r')
    linhas = produtostxt.readlines()
    cabecalhos = linhas[0]
    linhasAtualizadas = [cabecalhos]
    for linha in linhas[1:]:
        if codigo not in linha:
            linhasAtualizadas.append(linha)
    produtostxt.close()
    escreverTxt = open(caminho_absoluto,'w')
    escreverTxt.writelines(linhasAtualizadas)
    escreverTxt.close()
    return

def atualizarProduto():
    codigo = input('Código do produto a ser atualizado:')
    novoNome = input('Novo nome: ')
    novoPreco = input('Novo preço: ')
    novaQuantidade = input('Nova quantidade: ')

    caminho_relativo = 'produtos/produtos.txt'
    caminho_absoluto = os.path.abspath(caminho_relativo)

    # excluindo o produto
    produtostxt = open(caminho_absoluto, 'r')
    linhas = produtostxt.readlines()
    cabecalhos = linhas[0]
    linhasAtualizadas = [cabecalhos]
    for linha in linhas[1:]:
        if codigo not in linha:
            linhasAtualizadas.append(linha)
    produtostxt.close()
    escreverTxt = open(caminho_absoluto,'w')
    escreverTxt.writelines(linhasAtualizadas)

    # adicionando o produto com as informações atualizadas
    escreverTxt.writelines(f'{novoNome},{codigo},{novoPreco},{novaQuantidade}\n')
    escreverTxt.close()
    return

def listarPorNomes():
    caminho_relativo = 'produtos/produtos.txt'
    caminho_absoluto = os.path.abspath(caminho_relativo)
    produtos = ler_arquivo_produtos(caminho_absoluto)
    produtosSorted = sorted(produtos, key= lambda produto: produto['Nome'])
    for produto in produtosSorted:
        print(produto)
    return

def listarPorPrecos():
    caminho_relativo = 'produtos/produtos.txt'
    caminho_absoluto = os.path.abspath(caminho_relativo)
    produtos = ler_arquivo_produtos(caminho_absoluto)
    produtosSorted = sorted(produtos, key= lambda produto: float(produto['Preco']))
    for produto in produtosSorted:
        print(produto)
    return




