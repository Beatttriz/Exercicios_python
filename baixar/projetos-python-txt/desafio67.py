while True:
    num=int(input('Você quer a tabuada de qual número?'))
    if num < 0:
        break
    for c in range (1, 11):
        print ('{} x {} = {}'.format(num, c, num*c))
print('Pausa')
