valores=[]
max=0
min=0
for c in range(0,5):
    valores.append(int(input(f'Digite um valor {c}: ')))
    if c==0:
        max = min = valores[c]
    else:
        if valores[c] >max:
            max=valores[c]
        if valores[c] <min:
            min=valores[c]
print(f'Valores: {valores} ')
print(f'o maior é {max} posição ',end='')
for i, v in enumerate(valores):
    if v ==max:
        print(f'{i} ',end='')
print(f'e o menor {min} na posição ', end='')
for i, v in enumerate(valores):
    if v ==min:
        print(f'{i} ',end='')
