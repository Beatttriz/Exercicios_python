resp = 'S'
soma=quant=media = 0
while resp in 'Ss':
    n=int(input('Digite um valor: '))
    soma+=n
    quant+=1
    if quant ==1:
        maior=menor=n
    else:
        if n>maior:
            maior=n
        if n<menor:
            menor=n
    resp=str(input('Deseja continuar(S/N): ')).upper().strip()[0]
media=soma/quant
print('A média dos valores foi {} o maior é {} e o menor é {}'.format(media,maior,menor))