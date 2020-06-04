import random
a = input('Nome do primeiro aluno: ')
b = input('Nome do segundo aluno: ')
c = input('Nome do terceiro aluno: ')
d = input('Nome do quarto aluno: ')
names = [a, b, c, d]
print('O aluno escolhido é {}.'.format(random.choice(names)))
