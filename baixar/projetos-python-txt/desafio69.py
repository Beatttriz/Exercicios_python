tot18=toth=totm20=0
sexo=''
resp=''
while True:
    idade=int(input('Idade: '))
    if sexo != 'MF':
        sexo=str(input('Sexo: [F/M] ')).strip().upper()[0]
    if idade >=18:
        tot18+=1
    if sexo == 'M':
        toth +=1
    if sexo == 'F' and idade<20:
        totm20 +=1
    if resp != 'NS':
        resp=str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print(f'Total de +18 {tot18}')
print(f'Total de homens cadastrados {toth}')
print(f'Total mulheres -20 {totm20}')