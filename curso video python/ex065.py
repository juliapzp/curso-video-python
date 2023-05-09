resp = 'S'
soma = quant = media = maior = menor = 0
while resp in 'Ss':
    num = int(input('Digite um número: '))
    soma += num
    quant += 1
    if quant == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        elif num < menor:
            menor = num
    resp = str(input('Digite se quer continuar (S/N): ')).upper().strip()[0]
media = soma / quant
print(f'Você digitou {quant} números, e a média deles é {media}, o maior valor foi {maior} e o menor valor foi {menor}.')  