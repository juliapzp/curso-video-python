print('-' * 13)
print('Loja da Júlia')
print('-' * 13)
preco = float(input('Digite o preço das compras: '))
print('-' * 13)
print('''Formas de pagamento:
(1) À vista dinheiro/cheque
(2) À vista cartão
(3) 2x no cartão
(4) 3x ou mais no cartão''')
print('-' * 13)
opcao = int(input('Digite a opção: '))
if opcao == 1:
    total = preco - (preco * 10 / 100)
elif opcao == 2:
    total = preco - (preco * 5 / 100)
elif opcao == 3:
    total = preco
    parcela = total / 2
    print(f'Sua compra de {preco:.2f} será parcelada em 2x de R${parcela:.2f} sem juros e vai custar no final R${total:.2f}.')
elif opcao == 4:
    total = preco + (preco * 20 / 100)
    totalparc = int(input('Digite a quantidade de parcelas: '))
    parcela = total / totalparc
    print(f'Sua compra será parcelada em {totalparc}x de R${parcela:.2f} com juros de e vai custar no final R${total:.2f}.')
