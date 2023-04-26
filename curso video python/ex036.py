casa = float(input('Digite o valor da casa: R$'))
salario = float(input('Digite o salário do comprador: R$'))
anos = int(input('Digite quantos anos de financiamento: '))
prestacao = casa / (anos * 12)
minimo = salario * 30 / 100 
print(f'Para pagar uma casa de R${casa:.2f} em {anos}, a prestação será de R${prestacao:.2f}.')
if prestacao <= minimo:
    print('O empréstimo pode ser concedido.')
else:
    print('O empréstimo foi negado.') 