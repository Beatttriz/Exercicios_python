soma=0
media=0
maior=0
nome=''
tot=0
for p in range (1,5):
    print('-----{}° pessoa-----'.format(p))
    nomes=str(input('Nome: ')).strip()
    idade=int(input('Idade: '))
    sexo=str(input('Sexo [M/F]: ')).strip() 
    soma += idade
    if p==1 and sexo in 'Mm':
        maior=idade
        nome=nomes
    if sexo in 'Mm' and idade>maior:
        maior=idade
        nome=nomes
    if sexo in 'Ff' and idade<20:
        tot+=1
media=soma/4
print('A média de idades é {} anos'.format(media))
print('O homem mais velho tem {} anos e se chama {}'.format(maior,nome))
print(' Ao todo são {} mulheres com menos de 20 anos'.format(tot))