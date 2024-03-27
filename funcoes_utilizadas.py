#DEVER 1
def conta_vocal_consoante():
    vocais = 0
    conso = 0
    palavra = str(input("Digite uma palavra: "))
    for caracter in palavra.lower():
        if caracter in "aeiou":
            vocais += 1
        else:
            conso += 1
    
    print(f"numero de vocais: {vocais}")
    print(f"numero de consoantes: {conso}")

#DEVER 2        
def numeros2(num3,num4):#aqui estou dizendo que a minha função tem que receber 2 parametros(variaveis)
    soma2 = num3+num4
    return soma2

#DEVER 3    
def contador_palavras():
    texto = str(input("Digite um texto: "))
    contador = 0
    contador2 = texto.split()
    for umaChave in contador2:
        if umaChave in ".,;":
            print
        elif umaChave not in ".,;!?":
            contador += 1
    print(f"A quantidade de palavras utilizadas foi: {contador}")

#DEVER 4
def calculadora():
    while True :
        print("-"*100)
        escolha = int(input("Você acessou a calculadora!!! \n Soma digite 1: \n Subtração digite 2: \n Divisão digite 3: \n Multiplicação digite 4: \n Para sair Digite 5: \n"))
        print("-"*100)
        if escolha == 1:
            num1 = int(input("Digite o primeiro numero: "))
            num2 = int(input("Digite o segundo numero: "))
            soma = num1 + num2
            print(f"A soma do {num1} + {num2} = {soma}")
            print("-"*100)
        elif escolha == 2:
            num1 = int(input("Digite o primeiro numero: "))
            num2 = int(input("Digite o segundo numero: "))
            sub = num1 - num2
            print(f"A subatração de {num1} - {num2} = {sub}")
            print("-"*100)
        elif escolha == 3:
            num1 = int(input("Digite o primeiro numero: "))
            num2 = int(input("Digite o segundo numero: "))
            divisao = float
            divisao = num1/num2
            print(f"A divisão do {num1}/{num2} = {divisao}")
            print("-"*100)
        elif escolha == 4:
            num1 = int(input("Digite o primeiro numero: "))
            num2 = int(input("Digite o segundo numero: "))
            multi = float
            multi = num1*num2
            print(f"A multiplicação de {num1} x {num2} = {multi}")
            print("-"*100)
        else:
            break


#DEVER 5
def liga_desliga_lampada():
    interruptor = str(input("Ligar ou Desligar lampada: "))
    status = int
    if interruptor.lower() == "ligar":
        print("A lampada ligou!!")
        status = 1
    elif interruptor.lower() == "desligar":
        print("Lampada desligada!!!")
        status = 0
    return status
#DEVER 5
def status_lampada(status):
    if status == 1:
        print(f"A lampada esta ligada!!")
    else:
        print("A lampada esta desligada")
        


#DEVER 6    
def tabuada():
    numero = int(input("Digite o numero da tabuada: "))
    for umaChave in range(0,11):
        print(f"A tabuada do {numero} é {numero}*{umaChave} : {numero*umaChave}")
