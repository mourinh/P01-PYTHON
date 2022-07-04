mensagem_criptografada = ['8', '5', '-1', '7', '6', '-1', '8', '4', '-1', '7', '3', '-1', '7', '7', '-1', '6', '5', '-1']
frase = ''
palavra = ''

for letra in mensagem_criptografada:
    if letra != '-1':
        palavra += letra
    else:
        frase += chr(int(palavra))
        palavra = ''

print(frase)
