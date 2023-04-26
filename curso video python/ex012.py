preco = float(input('Digite um valor de um produto: R$'))
desconto = preco * 0.05
novo = preco - desconto
print(f'O produto que custava R${preco:.2f}, na promoção com desconto de 5% vai custar R${novo:.2f}.')