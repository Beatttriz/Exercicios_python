frase = str(input('digite uma frase: ')).upper().strip()
print('a letra a aparece{} vezes na frase.'.format(frase.count('A')))
print('a primeira letra a apareceu na posição {}.'.format(frase.find('A')+1))
print('a última letra a apareceu na posição {}.'.format(frase.rfind('A')+1))