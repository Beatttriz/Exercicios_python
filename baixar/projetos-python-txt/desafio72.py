cont=('zero', 'um','dois','três','quatro','cinco')
while True:
    num=int(input('Entre 0 e 5: '))
    if 0 <=num<=20:
        break
    print('Tente novamente.',end='')
print(f'Você digitou o número {cont[num]}')