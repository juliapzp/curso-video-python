n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))
opcao = 0
while opcao != 5:
    print('(1) Somar\n(2) Multiplicar\n(3) Maior\n(4) Novos Números\n(5) Sair do programa')
    opcao = int(input('Digite sua opção: '))
    print('-'*20)
    if opcao == 1:
        soma = n1 + n2
        print(f'A soma entre {n1} e {n2} é {soma}.')
    elif opcao == 2:
        mult = n1 * n2
        print(f'Multiplicando {n1} e {n2} o resuldado da {mult}.')
    elif opcao == 3:
        if n1 > n2:
            maior = n1
        elif n1 < n2:
            maior = n2
            print(f'Entre {n1} e {n2}, {maior} é o número maior.')
        elif n1 == n2:
            print('Os dois valores são iguais!')
    elif opcao == 4:
        print('Informe os números novamente.')
        n1 = int(input('Digite o primeiro valor: '))
        n2 = int(input('Digite o segundo valor: '))
    elif opcao == 5:
        print('Finalizando...')
    else:
        print('Opção inválida. Tente novamente:')
    print('-'*20)
print('Fim do programa.')