#Operadores de Comparação "==", "!=", ">", "<", ">=" e "<="
import time

valor_1 = 10

print(valor_1 == 10)
print(valor_1 != 8)
print(valor_1 > 1)
print(valor_1 < 20)
print(valor_1 >= 20)
print(valor_1 <= 20)

#Operadores Logicos "and", "or" "not"
valor_2 = 5
print(valor_2 > 3 and valor_2 > 1 ) # and para que o retorno seja true ambas afirmações tem que ser verdadeiras!
print(valor_2 > 1 and valor_2 > 10) # False

print(valor_2 > 2 or valor_2 > 8 ) # or para que retorne true uma das declarações tem que ser verdadeira
print(valor_2 == 5 or valor_2 > 10) # True
print(valor_2 >10  or valor_2 > 8) # False

lista_valor = [1,2,3,4] # in verifica se o valor existe ou não como exemplo abaixo
print(2 in lista_valor) # true valor consta dentro da lista!
print(10 in lista_valor) # false valor não consta na lista!

print(10 not in lista_valor) # negando se o valor esta dentro da lista ou seja 10 não consta na lista = true
print(2 not in lista_valor) # False 2 consta na lista

# Operadores de Identidade "is" e "is not"
String_01 = "Olá Felipe"
String_02 = "Olá Felipe"
print(type(String_01) is type(String_02)) #Compara se ambas as variaveis são strings = TRUE
print(type(String_01) is not type(String_02)) # Compara se ambas as variaveis são diferentes = FALSE

#Operadores de Associação "in" "not in" utiliza para validar uma sequencia em determinado objeto
lista_ações = ['Magalu', 'Via', 'Carrefour']
print("Via" in lista_ações) # true valida se a informações existe dentro da lista
print("Casa Bahia" in lista_ações) # false não existe tal informaçoes na lista

print("Casa Bahia" not in lista_ações) # true pois não existe tal informaçõa não lista
print("Via" not in lista_ações)# falso pois existe tal informações na nossa lista

#Manipulando Listas
#adicionar valor em uma lista append()
lista_vazia = []
print(lista_vazia)
lista_vazia.append(1)
lista_vazia.append(2)
lista_vazia.append(3)
lista_vazia.append("Valor Inserido")
print(lista_vazia)
print(len(lista_vazia)) # verificar o tamanho da lista após inserção de atributos na mesma

# Acessar lista por posição
print(lista_vazia[0])
print(lista_vazia[3])
print(lista_vazia[-2]) # informa o ultimo item da lista
print(lista_vazia[0:4]) # informa o range da lista de um ponto ao outro periodo que estou acessando

#clean() limpa a lista
print(lista_vazia)
# print(lista_vazia.clear())
print(lista_vazia)

#insert() inserir um valor na lista definindo a posição que deseja inserir o valor
lista_vazia.insert(3, 0) # incluindo um valor na posição 3 e o valor  0
lista_vazia.insert(0, 7)
print(lista_vazia)

#extend() inserir um lista dentro de outra lista
lista_01 = [1,2,3]
lista_02 = [4,5,6]
lista_01.extend(lista_02) #inseri a lista dois na lista um
print(lista_01) # Resultado : [1, 2, 3, 4, 5, 6]

#remove() remover um valor de uma lista
lista_01.remove(5)
print(lista_01) # removo um item da lista : [1, 2, 3, 4, 6], informando um numero ou palavra

# pop() removendo por possição
lista_01.pop(0)
print(lista_01) # removendo o valor pela posição dos valores atribuidos na lista : [2, 3, 4, 6]

# sort() ordenar valores
lista_abc = ['a', 'x', 'u', 'z', 'j']
lista_abc.sort()
print(lista_abc) # utilizando o comando sort(), o mesmo ordena a lista : ['a', 'j', 'u', 'x', 'z']

# reverse=True ordenando tambem o inverso dos valores
lista_abc.sort(reverse=True)
print(lista_abc) # Ordena a lista de forma inversa : ['z', 'x', 'u', 'j', 'a']

#copy() Copiar uma lista
lista_nova = lista_abc.copy()
print(lista_nova) # copia informações de uma determinada lista : ['z', 'x', 'u', 'j', 'a']

# index() indentificar um elemento dentro de uma lista mesmo que não saiba o valor
print(lista_nova.index("x")) # permite saber a posição do elemento dentro de uma lista : 1

#Pacotes Externos - DateTime
import datetime

Dia_Hoje = datetime.datetime.today() #Manupulando a data de Hoje através do datetime
print(Dia_Hoje) # imprime a data do dia corrente : 2022-04-16 21:00:39.804815, com modelo data e type data
print(type(Dia_Hoje))
print(datetime.datetime.today().date()) # Removendo a hora e passado apenas a data : 2022-04-16

# Construindo parametro de data
Data = datetime.datetime.today().date()
Ano = Data.year
Mes = Data.month
Dia = Data.day
print(Ano,Mes,Dia) #Montando a data por parametros dentro de variavies : 2022 4 16

#Contruindo uma data antiga com paramentro date()
Data_antiga = datetime.date(2022,4,13)
print(Data_antiga)# Contrução da data utilizando o parametro date() : 2022-04-13

#Calculo de datas
print(Data - Data_antiga) # calculo entre data pegando a danta atual mesmo a data antida: 3 days, 0:00:00

# strftime() Ajusta formatação de data do padão americano (ANO/MES/DIA) para o brasileiro (DIA/MES/ANO)
print(Data.strftime('%d/%m/%y')) # converter a data dia/mes/ano: 16/04/22

# Somar e diminuir data
print(Data + datetime.timedelta(days=30)) # Passando comando timedelta é ṕossivel somar uma para futura: 2022-05-16
print(Data - datetime.timedelta(days=20))

#time() Pacote externo
print('Comecei agora...')
time.sleep(3)
print("Terminei!")

#localtime()
Agora = time.localtime()
print(Agora)
print(type(Agora))
print(time.strftime('%m/%d/%y, %H:%M:%S', Agora)) #04/17/22, 16:20:49

#Conversão de data com o time.strptime
Time_texto = '21 June, 2021'
tt = time.strptime(Time_texto, '%d %B, %Y') # %B significa ajustes com base na configuração do pacote time
print(tt)

# math() Pacote externo ligado a operações matematicas
import math
Tupla = (10,20,30,40, 5)
print(min(Tupla)) #Pegar o menos valor dentro de uma tupla "5"
print(max(Tupla)) #Pegar o valor maximo dentro de uma tuppla "40"

#Conversão de numero - em numero +
print(abs(-1.76)) #Converte numero negativo em posito "1.76"

#Potencia
print(pow(3,4)) # calculo elevado a 4 potencia "3 * 3 * 3 * 3" = "81"

# Raiz Quadrada utilizando o pacote math
print(math.sqrt(81)) #Calcula o valor de raiz quadrada "9.0"

#Arredondamento
print(math.ceil(1.4)) # arredondamento para cima
print(math.floor(1.4))# arrendondamento para baixo
print(math.pi) # valor de pi "3.141592653589793"

#Pacote Externo Random
import random
ListaSequencia = [1,2,3,4,5,6,7,8,9]
sorteiaNnumero = random.choice(ListaSequencia) #utilizando o choice() é possivel pegar um numero aleatorio em uma lista
print(sorteiaNnumero)

Palavra = 'Felipe'
sorteiaPalavra = random.choice(Palavra)
print(sorteiaPalavra)

print(random.random()) #gerar numeros aleatorio valores entre 0 e 1 utilizando o random() "0.43068022580842"
print((random.randint(0, 5))) #gerar numero aleatorios dentre uma escala passada por parametro "2"

#statistics() Pacote Externo para estatistica
import statistics
Lista_media =[12,15,28,76,80,76]
print(sum(Lista_media) / len(Lista_media)) #validando uma mendia a soma das amostras validando pelo tamnhao da lista
print(statistics.mean(Lista_media)) # Forma mais simplificado ao exemplo de cima é utilizando o mean()
print(statistics.median(Lista_media)) # Validar o valor mediano de uma lista utilizando o median()
print(statistics.mode(Lista_media)) #Valida o valor que mais se repete dentre uma lista utilizando o mode()











