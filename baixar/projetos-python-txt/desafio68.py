from random import randint
v=total=0
tipo=''
while True :
    jog=int(input('Diga um valor '))
    comp=randint(0,10)
    total=jog+comp
    if tipo !='PI':
        tipo=str(input('Par ou ímpar? [P/I] ')).strip().upper()[0]
    print(f'Você jogou {jog} e o computador {comp}. Total de total {total}.',end='')
    print(' Deu par' if total% 2 ==0 else ' Deu ímpar')
    if tipo =='P':
        if total% 2 ==0:
            print('Venceu')
            v+=1
        else:
            print('Perdeu')
            break
    elif tipo =='I':
        if total% 2 ==0:
            print('Perdeu')
            v+=1
        else:
            print('Venceu')
    print('Vamo de novo')
print(f'Perdeu, você venceu {v} vezes')

