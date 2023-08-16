números=list()
while True:
    n=int(input('Digite um valor: '))
    if n not in números:
            números.append(n)
            print('valor adicionado')
    else:
         print('Duplicado não')
    r=str(input('Quer continuar? s/n'))
    if r in 'Nn':
        break
números.sort()
print(f'Você digitou os valores {números}')