matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
spar=mai=scol=0
for l in range(0,3):
    for c in range(0,3):
        matriz[l][c] = int(input(f'Valor [{l}, {c}]: '))
for l in range(0,3):
    for c in range(0,3):
        print(f'[{matriz[l][c]:^5}]', end='')
        if matriz[l][c] %2==0:
            spar +=matriz[l][c]
    print()
print(f'A soma dos pares é {spar}')
for l in range(0,3):
    scol +=matriz[l][2]
print(f'Soma da terceira coluna {scol}.')
for c in range(0,3):
    if c ==0:
        mai =matriz[1][c]
    elif matriz[1][c]>mai:
        mai=matriz[1][c]
print(f'O maior valor da segunda linha {mai}.')