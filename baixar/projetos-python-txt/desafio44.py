pre=float(input('Preço: R$'))
print('''FORMAS DE PAGAMENTO
[1] vista dinheiro/cheque
[2] vista cartão
[3] 2x no cartão
[4] 3x ou mais no cartão''')
op=int(input('Qual a opção? '))
if op==1:
    total=pre-(pre*10/100)
elif op==2:
    total=pre-(pre*5/100)
elif op==3:
    total =pre
    parcela=total/2
elif op ==4:
    total= pre+(pre*20/100)
    totparc=int(input('Quantas parcelas? '))
    parcela=total/totparc
else:
    total=0
    print('Opção inválida')
print('Sua compra de R${:.2f} vai custar R${:.2f}'.format(pre,total))
