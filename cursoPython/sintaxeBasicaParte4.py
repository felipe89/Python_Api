#Estrutura de Funções - só são utilizadas quando chamadas não alocando espaço na memoria
import random

def Boas_vindas():
    print("*******PYTHON********")

Boas_vindas()

#Exemplo de função usando uma função de soma
def Somar(Valor_1, Valor_2): # Defini o paramentro da minha função
    Soma = Valor_1 + Valor_2
    print(Soma)

Somar(1, 9) # Ao chamar a função defino os valores como passado no parametro da função porém o valor desejado da soma

# Chamando uma função dentro do Loop (FOR)
for Loop in range(0, 10):
    x = random.random()
    y = random.random()

    Somar(x, y)

#Estrutura Lambda
Funcao_Soma = lambda valor: valor + 10
print(Funcao_Soma(1))

Funcao_Soma_02 = lambda valor_1, valor_2 : valor_1 + valor_2
print(Funcao_Soma_02(10, 10))

#Exemplo 02
Exemplo = lambda valor : "Verdadeiro" if valor % 2 == 0 else "False"
print(Exemplo(4))

#Estrutura Try
try:
    0/0
    # print("Deu Certo!")
except:
    print("Não deu certo!")

finally:
    print('Vou ser executado da mesma forma!')



