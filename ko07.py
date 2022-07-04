produto_etiqueta = float(input('Preço da etiqueta do produto: R$'))
print('''FORMAS DE PAGAMENTO
[ 1 ] à vista DINHEIRO
[ 2 ] à vista CARTÃO CRÉDITO
[ 3 ] prazo 2x CARTÃO CRÉDITO
[ 4 ] prazo 3x ou mais CARTÃO CRÉDITO''')
tipo_pagamento = int(input('Digite o Tipo de pagamento: '))
if tipo_pagamento == 1:
    total = produto_etiqueta - (produto_etiqueta *0.15 / 100)
elif tipo_pagamento == 2:
    total = produto_etiqueta - (produto_etiqueta *0.10 / 100)
elif tipo_pagamento ==3:
    total = produto_etiqueta
    parcela = total / 2
    print('Sua compra será parcelada em 2x de R${:.2f} sem juros.'.format(parcela))
elif tipo_pagamento == 4:
    total = produto_etiqueta + (produto_etiqueta *0.20 / 100)
    totalparcelas = int(input('Quantas parcelas? '))
    parcela = total / totalparcelas
    print('Sua compra será parcelada em {}x de R${:.2f} com juros.'.format(totalparcelas, parcela))
else:
    total = produto_etiqueta
    print('Pagamento deu inválido. Tente mais uma vez.')
print('Sua compra é de R${:.2f} vai sair de R${:.2f} o pagamento.'.format(produto_etiqueta, total))

