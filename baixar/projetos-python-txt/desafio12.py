preço=float(input('Qual é o preço do produto? R$'))
novo=preço-(preço*5/100)
print('Custa com 5% de desconto R${:.2f}'.format(novo))