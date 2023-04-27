from random import randint
computador = randint(0, 10)
print('-'*10, 'Jogo de Adivinhação', '-'*10)
print('Acabei de pensar em um número entre 0 e 10, será que você consegue adivinhar qual foi?')
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Digite seu palpite: '))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Tente um número maior.')
        elif jogador > computador:
            print('Tente um número menor.')
print(f'Acertou com {palpites} tentativas. Parabéns!')
print('-'*41)
