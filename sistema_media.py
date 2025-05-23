#sistema de media de notas

print('SEJA BEM VINDO(A) AO SISTEMA DE NOTAS')
nome = input('digite o nome do aluno: ')

nota_mat = float(input('digite a nota de matematica: '))
nota_por = float(input('digite a nota de português: '))
nota_ing = float(input('digite a nota de inglês: '))

media = (nota_mat + nota_por + nota_ing) / 3
print ('o aluno',nome,'está com a média', media )

aprovado =media >=7
reprovado =media <5
recuperacao =media >=5 and media <7

print(f'''
o aluno {nome}
aprovado {aprovado}
reprovado {reprovado}
recuperação {recuperacao}
''')