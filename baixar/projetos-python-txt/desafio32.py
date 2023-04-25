ano = int(input('que ano quer analisar?'))
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 ==0 :
    print('o ano é bissexto')
else:
    print('não é bissexto')