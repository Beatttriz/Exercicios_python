s=float(input('salário: '))
if s <= 1250:
    novo= s+(s* 15/100)
else:
    novo = s + (s * 10 / 100)
print('seu novo sálario é {}'.format(novo))