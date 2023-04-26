from datetime import date
atual = date.today().year
nascimento = int(input('Digite o ano de nascimento: '))
idade = atual - nascimento
if idade <= 9:
    print('O atleta tem {idade} anos e está na classificação mirim.')
elif idade > 9 and idade <=14:
    print('O atleta tem {idade} anos e está na classificação infantil.')
elif idade <= 19:
    print('O atleta tem {idade} anos e está na classificação junior.')
elif idade <= 25:
    print('O atleta tem {idade} anos e está na classificação sênior.')
else:
    print('O atleta tem {idade} anos e está na classificação master.')