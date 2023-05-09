num = cont = soma = 0
num = (int(input('Digite um número (999 para parar): ')))
while num != 999:
    num = (int(input('Digite um número (999 para parar): ')))
    soma += num
    cont += 1
print(f'Você digitou {cont - 1} números e soma entre eles foi {soma - 999}.')