def dados():
    entrada_dados = int(input(f"Digite 1 para inserir nova chave: \n{"-"*45} \n Digite 2 para inserir nova definição: \n{"-"*45} \n Digite 3 para exibir o dicionario: \n{"-"*45} \n Digite 4 para deletar: \n{"-"*45} \n Digite 5 para sair!! \n{"-"*45} \n"))
    return entrada_dados

def adicionar_chave_elemento(dicionario):
    chave = str(input("Digite o nome da chave: "))
    valor = str(input("Digite um valor inicial: "))
    dicionario[chave] = [valor]
    print("="*45)
def adicionar_elementos(dicionario):
    chave2 = str(input("Escolha a chave: "))
    for umaChave2 in dicionario:
        if umaChave2 == chave2:
            valor2 = input("Digite um valor inicial: ")
            dicionario[umaChave2].append(valor2)
    print("="*45)
def excluir_elemento(dicionario):
    chave3 = str(input("Escolha a chave: "))
    for umaChave3 in dicionario:
        if umaChave3 == chave3:
            deletar = int(input("Digite o indice que vc quer deletar: "))
            dicionario[umaChave3].pop(deletar - 1)
    print("="*45)