from random import randint
num=(randint(1,10),randint(1,10),randint(1,10),randint(1,10),randint(1,10))
print('Valores',end='')
for c in num:
    print(f'{c}',end='')
print(f'O maior foi {max(num)} e o menor {min(num)}')