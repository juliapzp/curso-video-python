from datetime import date
atual = date.today().year
nasc = int(input('Digite o ano de nascimento: '))
idade = atual - nasc
print(f'Quem nasceu em {nasc}, tem {idade} anos em {atual}.')
if idade == 18:
    print('Você deve se alistar esse ano!')
elif idade < 18:
    saldo = 18 - idade
    print(f'Ainda faltam {saldo} ano(s) para o alistamento.')
elif idade > 18:
    saldo = idade - 18
    print(f'Você já deveria ter se alistado há {saldo} ano(s).')