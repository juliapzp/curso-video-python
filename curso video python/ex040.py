n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Dgitie a segunda nota: '))
media = (n1 + n2) / 2 
if 7 > media >= 5:
    print(f'Com as notas {n1} e {n2}, o aluno fica com a média {media:.2f} e está em recuperação.')
elif media < 5:
    print(f'Com as notas {n1} e {n2}, o aluno fica com a média {media:.2f} e está reprovado.')
else:
    print(f'Com as notas {n1} e {n2}, o aluno fica com a média {media:.2f} e está aprovado.')