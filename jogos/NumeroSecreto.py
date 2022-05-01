numero_segreto = 10

while True:
    numero = input("Informe um numero: ")

    try:
        numero = int(numero)
    except:
        print("Desculpe esse não é o numero secreto tente outra vez!")
        continue

    if numero != numero_segreto:
        if numero > numero_segreto:
            print(numero, "O numero informado é maior que o numero secreto tente outra vez!")

        elif numero < numero_segreto:
            print(numero, "O numero informado é menos que o numero secreto tente outra vez!")

        else:
            print("Você acertou parabens:", numero_segreto)
            break