palpites=0
from random import randint
computador = randint(1, 10)
print('-=-'*20)
print('vou pensar em um número entre 0 e 10...')
print('-=-'*20)
print('em que número eu pensei? ')
acertou=False
while not acertou:
    jogador=int(input('Qual seu paltite? '))
    palpites=palpites+1
    if jogador==computador:
        acertou= True
print('Conseguiu, após {} tentativa(s)'.format(palpites))
