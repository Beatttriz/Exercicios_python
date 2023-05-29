cont=n=soma=0
while True:
    n=int(input('Digite um número(para parar digite 999)'))
    if n == 999:
        break
    soma+= n
    cont+=1
print('Foram digitados {} cuja soma é {}'.format(cont,soma))