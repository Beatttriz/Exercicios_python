nome = str(input('Nome?'))
if nome == 'Bia':
    print('nome lindo')
elif nome == 'Pedro' or nome == 'Tiago' or nome == 'João':
    print('nome comum')
elif nome in 'Ana Maria':
    print('nome feminino comum')
else:
    print('Bem normal esse nome')
print('Bom dia, {}'.format(nome))