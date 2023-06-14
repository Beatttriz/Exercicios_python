total=totmil=menor=cont=0
barato = ''
resp=''
while True:
    produto=str(input('Nome do Produto: '))
    preço=float(input('Preço: R$'))
    cont+=1
    if preço>1000:
        totmil+=1
    if cont == 1:
        menor=preço
    else:
        if preço<menor:
            menor=preço
            barato=produto
    total+=preço
    resp=str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp=='N':
        break
print(f'Total R${total}')
print(f'{totmil} produto(s) mais de R$1000')
print(f'O produto mais barato foi {barato} que custa R${menor}')
