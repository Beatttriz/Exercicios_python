sexo=str(input('Qual seu sexo? [F/M] ')).strip().upper()
while sexo != 'F' and sexo != 'M':
    sexo=str(input('Erro, digite de novo ')).upper()
print('OK')