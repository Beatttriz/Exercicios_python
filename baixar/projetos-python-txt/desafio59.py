v1=int(input('Primeiro valor: '))
v2=int(input('Segundo valor: '))
op =0
while op!= 5:
    print('''ESCOLHA O QUE DESJA FAZER
    [1] Somar
    [2] Multiplicar
    [3] Maior
    [4] Novos números
    [5] Sair do programa''')
    op=int(input('Qual a opção? '))
    if op==1:
        soma=v1+v2
        print('A soma é {}'.format(soma))
    elif op==2:
        mult=v1*v2
        print('A multiplicação é {}'.format(mult))
    elif op==3:
        if v1>v2:
            print('O maior é {}'.format(v1))
        elif v1<v2:
            print('O maior número é {}'.format(v2))
        else:
            print('Os números são iguais')
    elif op ==4:
        v1=int(input('Primeiro valor: '))
        v2=int(input('Segundo valor: '))
print('Fim')
