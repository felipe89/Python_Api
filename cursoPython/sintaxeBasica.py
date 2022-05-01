# Imprimindo uma primeira linha de código em python
print("Bem vindo ao curso de Python!")
print("Ola Mundo! \nPulou uma linha")

# Operadores matematicos


# Tipo de Variaveis
nome = "Felipe"
Qualquer_Coisa = "Teste qualquer coisa!"
Var_text = str('String definada por type')
print(nome, Qualquer_Coisa, Var_text)

Var_Inteiro_1 =100
Var_inteiro_2 = int(20)
print(Var_Inteiro_1, Var_inteiro_2)

Var_Flutuante_1 = 10.90
Var_Flutuante_2 = float(1.5)
print(Var_Flutuante_1, Var_Flutuante_2)

Var_booleano_01 = True
Var_booleano_02 = False
print(Var_booleano_01, Var_booleano_02)

valor_1 = 2
valor_2 = 3
somaValores = valor_1 + valor_2
print(somaValores)

# Tipo de Dados
# Listas
Lista_Exemplo_01 = [1,2,3,4,5,6]
print("imprimindo minha lista",  Lista_Exemplo_01)

Lista_Exemplo_01 = [1,2,3,4,5,6]
print("imprimindo minha lista por posição",  Lista_Exemplo_01 [2])

#Lista combinada
Lista_Exemplo_02 = ["nome", "Sobrenome", "idade", 32]
print(Lista_Exemplo_02)

Lista_Exemplo_03 = ['Texte', 1, True, [1,2,3] ]
print(Lista_Exemplo_03)

# Tuplas ---> São imutaveis
Tupla_Exemplo_01 = (1,2,3,4,5,6)
Tupla_Exemplo_02 = ("Texto", True, 2, 2.0)
print("Imprimindo Tupla 01", Tupla_Exemplo_01, "Imprimindo Tupla 02 ", Tupla_Exemplo_02)

#Dicionario
Dicionario = {
    'Index' : 'valor',
    'id' : 1,
    'id' : 2,
    'Nome': "Teste",
    'Lista': Lista_Exemplo_01,
    'Tupla': Tupla_Exemplo_01
}
print("Imprimindo dicionario ", Dicionario)

#Nomeação de variaveis
#Nomeação separado por virgula
Laranja, Melao, Limao = 1, 2, 3
print("Imprimindo variaveis na mesma linha", Laranja,Melao,Limao)

#Nomeação mesmo valor para variaveis diferentes
Morango = Uva = Maca = 100
print("Imprimir variavel com valor global", Morango, Uva , Maca)

#Nomeação por Listas
Lista_Carros = ['VW', 'Audi', 'Ford']
Marca_01, Marca_02, Marca_03 = Lista_Carros
print("Imprimindo valores de uma lista atribuido para cada variavel ", Marca_01, Marca_02, Marca_03)

#Nomeação combinação de variaveis
Nome = 'Felipe'
Sobrenome = 'Trindade'
NomeCompleto = Nome +' '+Sobrenome
print("Imprimindo combinação de variaveis", NomeCompleto)

#Experimento (Conversão de inteiro em uma string)
Nome_01 = 'Felipe'
Idade_01 = str(32)
print(Nome_01 +' '+ Idade_01 + " anos")

#Experimento (Conversão ponto flutuante FLOAT)
Invertimento = 1000
Taxa_Juros = float('0.2')
print(Invertimento * Taxa_Juros)

Valor_Ganho = (Invertimento * Taxa_Juros) + Invertimento
print(Valor_Ganho)

# Tipo da Informações
String = str("Ola Mundo!")
Inteiro = int(10)
Flutuante = float(1.4)
Complex = complex(1j)
Lista = list(('Maça', 'Morango'))
Tupla = tuple(('A', 'B'))
Range = range(3)
Dicionario_1 = dict(nome='Felipe', age=32)
Set = set(('A','B', 'C'))
Fronzet = frozenset(('A', 'B', 'C'))
Boleano = bool(5)
Bytes = bytes(5)
ByteArray = bytearray(5)
Memoryview = memoryview(bytes(5))

from datetime import datetime
Data = datetime.today().date()

#Comando Round - Diminui a quantidade de casa decimais utilizadas ou arredonda para o valor mais proximo
Valor_Exemplo = 12.209120930
print(Valor_Exemplo)

print(round(Valor_Exemplo, 4))

#Comando Len - Retonar a quantidade de elementos e calcular o tamanho de algum elemento
Lista = [1,2,3,4,5,6,7,8,9,10]
Dicionario_2 = {'Nome':'Felipe', 'Idade': 32}
Tupla_2 = (1,2,3)
String_2 = 'Olá Mundo!'

print(len(Lista))
print(len(Dicionario_2))
print(len(Tupla_2))
print(len(String_2))

#Fatiamento de Strings
Minha_String = 'Aprendendo Python!'
print(type(Minha_String))
print(len(Minha_String))

print("Pegando string por posição " + Minha_String[0])
print("Pegando string de um ponto a outro " + Minha_String[0:10])
print("Pegando string pela ultima posição " + Minha_String[-10])

CPF ='32064698848'
print("Pegando a posição dentro da variavel CPF " + CPF[9])

#Manipulação de Strings
#Replace() substituir algo
String_replace = "Olá Mundo!"
print(String_replace)

String_replace.replace('Mundo', 'Mundão')
print('Utilizanção o replace para substituir o final de uma string: ' + String_replace.replace('Mundo', 'Mundão'))
print(CPF.replace('32064698848', '111222333355'))

#Startswuith() verificar se a nossa string começa com alguma coisa
String_starswuith = 'Olá Felipe'

#verifica o começo da string
print(String_starswuith.startswith('Olá'))
print(String_starswuith.startswith('Felipe'))

#endswuith() verifica o final da string
print(String_starswuith.endswith('Felipe'))
print(String_starswuith.endswith('Olá'))

# count() Contar Palavras
print(String_starswuith.count("e"))

# capitalize() Transformação nos textos de minusculo para maiusculo
Nome_capitalize = 'felipe'
print(Nome_capitalize.capitalize())

#isdigit() Verificar se existe!
CPF_Digit = '11244533211'
print(CPF_Digit.isdigit()) # verificando se a minha string possui valor numerico

CPF_Digit_2 = '112335118AB'
print(CPF_Digit_2.isdigit()) # resultado falso o isdigit verifica só se o valor é numerico

# isalnum() Verificar se uma string é alfanumerico
String_alfnumerico = 'Olá Felipe'
print(String_alfnumerico.isalnum()) # Resultado será falso pois tem que ser apenas valores letras e numeros

# upper() Deixer uma string minuscula em maiuscula
String_upper = 'ola felipe'
print(String_upper.upper())

#lower() transformar uma string maiuscula em minuscula
String_lower ='OLA FELIPE'
print(String_lower.lower())

# find() Localizar alguma coisa especifica na string
Frase = 'Hoje esta muito frio!'
print(Frase.find('muito'))
print(Frase.find('!'))
print(Frase.find('palavra não existe'))

# strip() remover espaços entre as palavras
String_Endereco = '     Rua Galaxia numero 955  '
print(String_Endereco.strip())

#split() quebra a string em pedaços de acordo que queremos
String_Split = 'Rua Galaxia, 955, Jardim Santa Barbara'
print(String_Split.split(",")) # separação por virgula utilizada na string
print(String_Split.split(" ")) # separa pelo espaço da string

#Comando input
input("Entre com o seu nome: ")

# Exemplo do uso do input
Nome = input("Qual o seu nome: ")
Idade = input("Qual a sua idade: ")
print("Seu nome é: ", Nome)
print("Sua idade é: ", Idade)