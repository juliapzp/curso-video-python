peso = float(input('Digite o peso (kg):'))
altura = float(input('Digite a altura (m):'))
imc = peso / (altura ** 2)
print(f'O IMC dessa pessoa é de {imc}')
if imc < 18.5:
    print('O peso está abaixo da faixa de peso normal.')
elif 18.5 <= imc < 25:
    print('O peso está na faixa de peso normal.')
elif 25 <= imc < 30:
    print('O peso está na faixa de sobrepeso.')
elif 30 <= imc < 40:
    print('O peso está na faixa de obesidade, cuidado!')
elif imc >= 40:
    print('O peso está na faixa de obesidade mórbida.')


