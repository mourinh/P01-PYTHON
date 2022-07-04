altura = float(input("Digite seu altura: "))
sexo = input("Digite seu sexo: ")

if sexo == 'H':
    resultado = (72.7 * altura) - 58
elif sexo == 'M':
    resultado = (62.1 * altura) - 44.7

print("{:.2f}".format(resultado))
