soma=0
for c in range (1,7):
    num=int(input('Digite um número'))
    if c%2==0:
        soma=soma+num
print('A soma dos números pares é {}'.format(soma))
