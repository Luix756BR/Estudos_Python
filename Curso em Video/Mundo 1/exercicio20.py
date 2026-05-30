from random import shuffle 
a1 = input('Diga quem é o primeiro aluno:')
a2 = input('Diga quem é o segundo aluno:')
a3 = input('Diga quem é o terceiro aluno:')
a4 = input('Diga quem é o quarto aluno:')
lista = [a1,a2,a3,a4]
shuffle(lista)
print('A ordem de apresentação desses alunos será {}'.format(lista))