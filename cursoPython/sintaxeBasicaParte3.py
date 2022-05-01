#Condicionais IF / ELSE
import random

Idade = 18   #Condição se a pessoa tiver menos que 18 anos ela não entra no sistema

if Idade >= 18:
    print("Voce pode entrar, pois é maior de idade!")

# Else
Idade = 10

if Idade >= 18:
    print("Voce pode entrar, pois é maior de idade!")
else:
    print("Voce é menos de idade não pode entrar!")

#ELIF
Idade = 15

if Idade >= 18:
    print("Voce pode entrar, pois é maior de idade!")
elif Idade >= 15 and Idade <= 17:
    print("Seu Pai ou Mãe pode autorizar a entrada!")
else:
    print("Voce é menos de idade não pode entrar!")

#Estrutura de loop FOR
for QualquerCoisa in range(5):
    print("Entrei no FOR", QualquerCoisa) #Criação de um for (Loop), para executar a quantidade de vez que esta em parametro

for OutraCoisa in range (5):
    print("Operações dentro do FOR", OutraCoisa * 3) #Posso incrementar o for como desejar

for OutraCoisa in range (1, 5):
    print("Passando parametro no RANGE ", OutraCoisa * 3) #o Range pode ser ajustado devido o parametro passado

#Combinando o for dentro de listas
Lista = ["Brasil", "Argentina", "Uruguai", "Paraguai", "Bolivia", "Colombia", "Equador"]

for PercorrerLista in Lista:
    print("Percorrendo uma lista dentro do FOR: ", PercorrerLista)

for PercorrerLista in Lista:
    print("Utilizando o upper(): ", PercorrerLista.upper())

for PercorrerLista in Lista:
    print("Utilizando por possição: ", PercorrerLista[0:3])

for PercorrerLista in Lista:
    print("Utilizando o lower() ", PercorrerLista.lower())

for PercorrerLista in Lista:
    print("Utilizando o upper() e abreviação ", PercorrerLista.upper()[0:3])

#Utilizando condicionais IF junto com o FOR
for Pais in Lista:

    if Pais == "Uruguai":
        print("Pais bi-campeão da copa do mundo!")

#Utilizando o FOR dentro de um outro FOR
for Pais in Lista:

    if Pais == "Uruguai":
        print("Pais bi-campeão da copa do mundo!")

        for AlgumaCoisa in range(5):
            print(AlgumaCoisa)

#Outra Forma de acessar uma lista maneira mais interativa
for loop in range(0, len(Lista), 2): #Fazendo a lista pular de dois em dois e retornar o resultado
    print(Lista[loop])

for loopDois in range(len(Lista)): #Pegando as informações de uma lista por posição
    print(loopDois)

# For utilizando o parametro enumerate()
for index, Pais in enumerate(Lista): #Enumera os elementros dentro de uma lista "0 Brasil", "1 Argentina"
    print(index, Pais)

# Outra forma de enumeração de elementos dentro de uma lista
x = 0

for Pais in Lista:
    print("Enumerando uma lista dentro do for de outra maneira: ", x, Pais)
    x+=1

# Utilizar o for dentro de uma lista
ListaFor = [Numero for Numero in range(0,10)]
print(ListaFor)

# Loops utilizando While
Parar = 0

while Parar <= 5:
    print("Usando o While", Parar)
    Parar += 1

# Utilizando o While  com condicional e FOR
# loop = 0
#
# while loop <= 10:
#
#     print(loop)
#
#     if loop == 5:
#         for x in range(10):
#             print(x)
#             loop += 1

#Jogo utilizando while random e condicional
while True:
    Eu = random.randint(0, 10)
    Contra_Voces = random.randint(0, 10)

    print("Eu tirei o valor: ", Eu)
    print("Voces tiraram o valor: ", Contra_Voces )

    if Eu > Contra_Voces:
        print("Ganhei!!!!")
        break
        print('\n')

#Estrutura de quabra com Break e Continue
#Exemplo BREAK
Lista_1 = ['morango', 'pera', 'uva', 'abacaxi', 'banana']

for Fruta in Lista_1:
    print(Fruta)

    if Fruta == 'uva':
        break

#Exemplo CONTINUE
for LoopNumero in range(0, 11):

    if LoopNumero == 5:
        continue #Ele não entra na condicional e apenas continua o loop diferente do break que pararia na condicional
        print("Cheguei aqui mais serei ignorado!")

    print(LoopNumero)


