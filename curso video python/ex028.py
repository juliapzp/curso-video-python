from random import randint
from time import sleep
computador = randint(1, 5)
print('-' * 55)
print('Vou pensar em um número de 1 à 5, tente adivinhar...')
print('-' * 55)
print('Em que número eu pensei?')
jogador = int(input('Digite: '))
print('Processando...')
sleep(1)
if jogador == computador:
    print('Parabéns! Você acertou!')
else:
    print(f'Você errou... Pensei no número {computador} e não no {jogador}.')