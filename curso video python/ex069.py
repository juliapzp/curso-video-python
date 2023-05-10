tot18 = toth = totm20 = 0
print('-'*20)
print('Análise de grupo')
print('-'*20)
while True:
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MmFf':
        sexo = str(input('Sexo: ')).strip().upper()[0]
    if idade >= 18:
        tot18 += 1
    if sexo == 'M':
        toth += 1
    if sexo == 'F' and idade < 20:
        totm20 += 1


    resp = ' '
    while resp not in 'SsNn':
        resp = str(input('Quer continuar? (S/N): ')).strip().upper()[0]
    if resp == 'N':
        break
print('-'*20)
print('Análise: ')
print(f'Total de pessoa com mais de 18 anos: {tot18}\nTotal de homens: {toth}\nTotal de mulheres com menos de 20 anos: {totm20}')
print('-'*20)