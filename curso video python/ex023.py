num = int(input('Digite um número: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print(f'Analisando o número {num}')
print(f'Sua unidade é {u};')
print(f'Sua dezena é {d};')
print(f'Sua centena é {c};')
print(f'Seu milhar é {m}.')