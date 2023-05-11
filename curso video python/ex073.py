tabela = ('Flamengo', 'Internacional', 'Atlético Mineiro', 'São Paulo', 'Fluminense', 'Grêmio', 'Palmeiras', 'Santos', 'Athletico-PR', 'Corinthians', 'Bragantino', 'Ceará', 'Atlético-GO', 'Sport', 'Bahia', 'Fortaleza', 'Vasco da Gama', 'Goiás', 'Coritiba', 'Botafogo')
print('*-=' * 98)
print(f'Lista de Times do Brasileirão 2021: {tabela}')
print('*-=' * 98)
print('Os 5 primeiros são: ')
for c in range(0, len(tabela) - 15):
    print(f'{c + 1}° {tabela[c]}')
print('*-=' * 7)
print('Os 4 últimos são:')
for pos, c in enumerate(tabela[16:]):
    pos += 17
    print(f'{pos}° {c}')
print('*-=' * 95)
print(f'Times em ordem alfabética: {sorted(tabela)}')
print('*-=' * 95)
palmeiras = tabela.index('Palmeiras')
print(F'O Palmeiras está na {palmeiras + 1} posição')