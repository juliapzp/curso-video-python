total = totmil = menor = cont = 0
barato = ' '
while True:
    produto = str(input('Nome do produto: '))
    preco = float(input('Preço do produto: R$'))
    cont += 1
    total += preco
    if preco > 1000:
        totmil += 1
    if cont == 1 or preco < menor:
        menor = preco
        barato = produto
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? (S/N): ')).strip().upper()[0]
    if resp == 'N':
        break
print('Fim do programa.')
print(f'O total da compra foi R${total:.2f}.')
print(f'Temos {totmil} produtos custando mais de R${totmil:.2f}.')
print(f'O produto mais barato custa R${menor:.2f}')