velocidade = float(input('Qual é a velocidade atual do carro? '))
multa = (velocidade - 80) * 7
if velocidade > 80:
    print(f'Você excedeu o limite de 80km/h!\nVocê irá pagar uma multa de R${multa:.2f}.')
else: 
    print('Parabéns! Está abaixo do limite de 80km/h.')