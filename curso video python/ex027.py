n = str(input('Digite seu nome completo: ')).strip()
nome = n.split()
primeiro = nome[0]
ultimo = nome[len(nome) - 1]
print(f'Seu primeiro nome é {primeiro} e o último nome é {ultimo}.')