galera=list()
dado=list()
totgo=totma=0
while True:
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Peso: ')))
    galera.append(dado[:])
    dado.clear()
    r=str(input('Quer continuar? s/n '))
    if r in 'Nn':
        break
for p in galera:
    if p[1]>=90:
        print(f'{p[0]} está acima do peso')
        totgo += 1
    else:
       print(f'{p[0]} está abaixo do peso')
       totma += 1
print(f'Temos {totgo} pessoa(s) gorda(s) e {totma} pessoa(s) magra(s).')