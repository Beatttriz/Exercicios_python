cont=0
n=0
soma=0
while n != 999:
    n=int(input('Digite um número(para parar digite 999)'))
    soma+= n
    cont+=1
print('Foram digitados {} cuja soma é {}'.format(cont-1,soma-999))