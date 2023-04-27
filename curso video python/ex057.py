sexo = str(input('Informe seu sexo (M/F): ')).strip().upper()[0]
while sexo not in 'MF':
    sexo = str(input('Dados inválidos. Informe seu sexo novamente: ')).strip().upper()[0]
print(f'Sexo {sexo} foi registrado com sucesso.')
