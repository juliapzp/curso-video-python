salario = float(input('Qual o valor do salário? '))
if salario <= 1250:
    novo = salario + (salario * 15 / 100)
else:
    novo = salario + (salario * 10 / 100)
print(f'O salário de R${salario:.2f}, passou a ser R${novo:.2f} agora com o aumento.')