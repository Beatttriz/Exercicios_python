valores=[]
while True:
    valores.append(int(input('Digite um valor: ')))
    resp=str(input('Continuar? (s/n)) '))
    if resp in 'Nn' :
        break
print(f'Você digitou {len(valores)} elementos')
valores.sort(reverse=True)
print(f'Os valores em ordem decrescentes são {valores}')