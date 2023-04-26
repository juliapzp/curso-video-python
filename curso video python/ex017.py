from math import hypot
co = float(input('Digite o comprimento do cateto oposto: '))
ca = float(input('Digite o comprimento do cateto adiacente: '))
#hi = (co ** 2) (ca ** 2) ** (1/2)
hi = hypot(co, ca)
print(f'A hipotenusa vai medir: {hi:.2f}')