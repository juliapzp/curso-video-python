from math import radians, sin, cos, tan
angulo = float(input('Digite o ângulo: '))
seno = sin(radians(angulo))
cosseno = cos(radians(seno))
tangente = tan(radians(angulo))
print(f'O ângulo de {angulo}° tem o seno de {seno:.2f}, o cosseno de {cosseno:.2f} e o a tangente de {tangente:.2f}')
