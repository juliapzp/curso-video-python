from random import randint
print('Jogo de par ou ímpar')
print('-'*20)
while True:
    jogador = int(input('Digite um valor: '))
    computador = randint(1, 11)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PpIi':
        tipo = str(input('Par ou ímpar? (P/I): ')).strip().upper()[0]
    print(f'Você jogou {jogador} e o computador jogou {computador}. O total foi de {total}.')
    if tipo == 'P':
        if total % 2 == 0:
            print('Você venceu!')
        else:
            print('Você perdeu!')
    elif tipo == 'I':
        if total % 2 == 0:
            print('Você perdeu!')
        else:
            print('Você ganhou!')
