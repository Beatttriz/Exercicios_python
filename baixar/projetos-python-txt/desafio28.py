from random import randint
from time import sleep
computador = randint(0, 5)
print('-=-'*20)
print('vou pensar em um número entre 0 e 5...')
print('-=-'*20)
jogador=int(input('em que número eu pensei? '))
sleep(3)
if jogador == computador:
    print('você venceu')
else:
    print('você perdeu, eu pensei no {}'.format(computador))