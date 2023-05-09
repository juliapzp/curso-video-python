print('-' * 13)
print('Gerador de PA')
print('-' * 13)
primeiro = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão da PA: '))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total :
        print(f'{termo} -> ', end= '')
        termo += razao
        cont += 1
    print('Pausa')
    mais = int(input('Digite quantos termos você quer mostrar a mais: '))
print('Fim')