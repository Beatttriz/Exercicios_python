galera=list()
pessoa=dict()
soma=media=0
while True:
    pessoa.clear()
    pessoa['nome']=str(input('Nome: '))
    while True:
        pessoa['sexo']=str(input('Sexo: m/f ')).upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('Erro')
    pessoa['idade'] =int(input('Idade: '))
    soma+=pessoa['idade']
    galera.append(pessoa.copy())
    while True:
        resp=str(input('Quer continuar? s/n ')).upper()[0]
        if resp in 'SN':
            break
        print('Erro')
    if resp == 'N':
        break
print(f'Ao todo temos {len(galera)} pessoas cadastradas')
media=soma/len(galera)
print(f'B) média de idade é {media} anos')
print('C) As mulheres ',end='')
for p in galera:
    if p ['sexo'] in 'F':
        print(f'{p["nome"]}',end='')
print()