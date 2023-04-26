frase = str(input('Digite uma frase: ')).upper().strip()
vezes = frase.count('A')
pri = frase.find(('A')) + 1
ult = frase.rfind(('A')) + 1
print(f'A letra "A" aparece {vezes} vezes na frase;')
print(f'A primeira letra "A" apareceu na {pri} posição;')
print(f'A última letra "A" apareceu na {ult} posição.')
