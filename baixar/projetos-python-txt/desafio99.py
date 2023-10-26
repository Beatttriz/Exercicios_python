def maior(* num):
    cont=maior=0
    for valor in num:
        print(f'{valor} ', end='', flush=True)
        if cont ==0:
            maior=valor
        else:
            if valor>maior:
                maior=valor 
        cont+=1
    print(f'Foram informados {cont} valores')
    print(f'O maior valor foi {maior}')

maior(2,3,12,10)
maior(1)
maior()