from funcoesdodesafio import dados,adicionar_chave_elemento,adicionar_elementos,excluir_elemento
dicionario = {}
while True:
    entrada_dados = dados()
    if entrada_dados == 1:
        adicionar_chave_elemento(dicionario)
        #lembrar de por entre conchetes 
    elif entrada_dados == 2:
        adicionar_elementos(dicionario)
    elif entrada_dados == 3:
        for umaChave in dicionario:
            print(f"{umaChave} - {dicionario[umaChave]}")
    elif entrada_dados == 4:
        excluir_elemento(dicionario)
    elif entrada_dados == 5:
        break