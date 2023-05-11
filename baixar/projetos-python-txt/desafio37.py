num=int(input('Digite um número inteiro: '))
print('''Escolha uma das bases para conversão: 
[1] binário
[2] octal
[3] hexadecimal''')
op=int(input('Sua opção: '))
if op ==1:
    print('{} convertido para binário é {}'.format(num, bin(num)))
elif op ==2:
    print('{}  convertido para octal é {}'.format(num, oct(num)))
elif op ==3:
    print('{} convertido para hexadecimal é {}'.format(num, hex(num)))
else:
    print('Opção inválida')