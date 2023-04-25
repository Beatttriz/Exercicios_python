d=float(input('qual a distância? '))
preço=d * 0.50 if d <= 200 else d * 0.45
print('valor da passagem R${:.2}' .format(preço))