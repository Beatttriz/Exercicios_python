sexo=str(input('Qual seu sexo? [F/M] ')).strip().upper()[0]
while sexo not in 'MmFf':
    sexo=str(input('Erro, digite de novo ')).upper().strip()[0]
print('OK')