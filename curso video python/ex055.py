maior = 0
menor = 0
for p in range(1, 6):
    peso = float(input(f'Informe o peso da {p}° pessoa: '))
    if p == 1:
        maior = peso
        menor = peso
    else: 
        if peso > maior:
            maior = peso
            menor = peso
        else:
            if peso > maior:
                maior = peso
            if peso < maior:
                menor = peso
print(f'O maior peso lido foi de {maior}kg')
print(f'O menor peso lido foi de {menor}kg')