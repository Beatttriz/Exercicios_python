from random import randint
itens=('pedra','papel','tesoura')
comp=randint(0,2) 
print('''Suas opções
[0] pedra
[1] papel
[2] tesoura''')
Jogador = int(input('Qual é a sua jogada? '))
print('O computador jogou {}.'.format(itens[comp]))
print('O jogador jogou {}.'.format(itens[Jogador]))
if comp ==0: 
    if Jogador==0:
        print('Empate')
    elif Jogador ==1:
        print('Jogador vence')
    elif Jogador ==2:
        print('Computador vence')
    else:
        print('Jogada inválida')
elif comp ==1:
    if Jogador==1:
        print('Empate')
    elif Jogador ==2:
        print('Jogador vence')
    elif Jogador ==0:
        print('Computador vence')
    else:
        print('Jogada inválida')
elif comp ==2:
    if Jogador==2:
        print('Empate')
    elif Jogador ==0:
        print('Jogador vence')
    elif Jogador ==1:
        print('Computador vence')
    else:
        print('Jogada inválida')
