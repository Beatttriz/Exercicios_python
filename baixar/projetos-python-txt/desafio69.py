tot18=toth=totm20=0
while True:
    idade=int(input('Idade: '))
    sexo=str(input('Sexo [F/M] '))
    if idade>=18:
        tot18+=1
    if sexo =='M':
        toth+=1
    if sexo == 'F' and idade <20:
        totm20 +=1
    resp=str(input('Quer continuar[S/N] '))
    if resp == 'N':
        break
print(f'Total com mais de 18 {tot18}')
print(f'Homens cadastrados {toth}')
print(f'Mulheres com menos de 20 {totm20}')