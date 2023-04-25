velocidade = float(input('qual é a velocidade atual do carro?'))
if velocidade > 80:
    print('multado, o limite de velocidade é 80km')
    multa= (velocidade-80) * 7
    print('sua multa vai custar R${:.2f}:'.format(multa))
else:
    print('dirija com segurança')