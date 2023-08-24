time=list()
jogador=dict()
partidas=list()
while True:
    jogador.clear()
    jogador['nome']=str(input('Nome do jogador: '))
    tot=int(input(f'Partidas? '))
    partidas.clear()
    for c in range(0, tot):
        partidas.append(int(input(f'Quantos gols na partida {c}? ')))
    jogador['gols']=partidas[:]
    jogador['total']=sum(partidas)
    time.append(jogador.copy())
    resp=str(input('Quer continuar? s/n ')).upper()[0]
    if resp == 'N':
        break
print('cod', end='')
for i in jogador.keys():
    print(f'{i}', end='')
print()
for k, v in enumerate(time):
    print(f'{k}', end='')
    for d in v.values():
        print(f'{str(d)}', end='')
    print()
while True:
    busca=int(input('Mostrar dados de qual jogador? 999 para parar'))
    if busca == 999:
        break
    if busca>=len(time):
        print(f'Erro')
    else:
        print(f'Jogador {time[busca]["nome"]}: ')
        for i, g in enumerate(time[busca]['gols']):
            print(f'No jogo {i+1} fez {g} gols')