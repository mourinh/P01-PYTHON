altura = float(input('Digite sua altura: '))  
peso = float(input('Digite  seu peso: ')) 

imc = peso/(altura * altura)  

if imc < 18.5:
    print('Pessoa abaixo do peso')
elif 18.5 < imc > 25:
    print('Pessoa com peso normal')
elif 25 < imc > 30:
    print('Pessoa acima do peso')
elif imc > 30:
    print('Pessoa Obesa')

print("{:.2f}".format(imc))