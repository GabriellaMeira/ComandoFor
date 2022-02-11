# testar comando for:
import random

def testarComandofor():
    nomes = ["Cao", "Magalhães", "Lúcio", "Nelson", "Sophia"]
    print("Nomes armazenados na lista:")
    for cont in nomes:
        print(cont)

def testarRange():
    # range(10): uma sequência de números de 0 a 9
    # range(1,10): uma sequência de números de 1 a 9
    # range (1,10,2): uma sequência de uúmeros de 1 a 9, 2 a 2
    # número 2 significa intervalo
    for cont in range(1,10,2):
        print(f"{cont}:Seja bem vindo a Linguagem Python!")

def exibirMegaSena(num):
    for i in range(num):
        numMegaSena = random.randrange(1,61)
        print(f"{i+1}o Número gerados: {numMegaSena}")

def listaMegaSena(num):
    mega_sena = [] # ou mega_sena = list()
    for i in range(num):
        numMegaSena = random.randrange(1,61)
        mega_sena.append(numMegaSena) # adicionar numMegaSena na lista
    print(mega_sena)

def contaletras():
    frase = "Pessoal, vamos jogar tenis!"
    qtdcaracteres = 0
    for letra in frase:
        qtdcaracteres += 1
    print(qtdcaracteres)

def forAnhinhado(num):
    for i in range(num):
        for j in range(num):
            print("Mensagens")

#programa principal
#testarComandofor()
#testarRange()
#numero = int(input("Informe a quantidade de números a serem gerados para Mega Sena: "))
#exibirMegaSena(numero)
#listaMegaSena(numero)
#contaletras()
numero = int(input("Informe um número inteiro "))
forAnhinhado(numero)
input("fim")
