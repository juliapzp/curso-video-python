from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0,2)
print('''Opções:
(0) Pedra
(1) Papel
(2) Tesoura''')
jogador = int(input('Digite a sua jogada: '))
sleep(1)
print('-'*10)
print(f'O computador jogou {itens[computador]}')
print(f'O jogador jogou {itens[jogador]}')
print('-'*10)
sleep(1)
if computador == 0: #computador jogou pedra
    if jogador == 0:
        print('Empate.')
    elif jogador == 1:
        print('Jogador venceu.')
    elif jogador == 2:
        print('Computador venceu.')
    else:
        print('Jogada inválida.')
elif computador == 1: #computador jogou papel
    if jogador == 0:
        print('Computador venceu.')
    elif jogador == 1:
        'Empate.'
    elif jogador == 2:
        print('Jogador venceu.')
    else:
        print('Jogada inválida.')
elif computador == 2: #computador jogou tesoura
    if jogador == 0:
        print('Jogador venceu.')
    elif jogador == 1:
        print('Computador venceu.')
    elif jogador == 2:
        print('Empate.')
    else:
        print('Jogada inválida.')