dist = float(input('Qual é a distância da sua viagem? '))
print(f'Você está prestes a começar uma viagem de {dist}km.')
if dist <= 200:
    preco = dist * 0.5
else:
    preco = dist * 0.45
print(f'O preço de sua passagem será de R${preco:.2f}.')