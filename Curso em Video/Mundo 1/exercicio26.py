n = input('Digite sua frase: ').strip()
print('A letra "A" aparece {} vezes nessa frase'.format(n.upper().count('A')))
print('A letra "A" aparece pela primeira vez na posição {} dessa frase'.format(n.upper().find('A')+1))
print('A letra "A" aparece pela última vez na posição {} dessa frase'.format(n.upper().rfind('A')+1))