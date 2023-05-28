primeiro=int(input('primeiro termo: '))
r=int(input('razão: '))
t=primeiro
cont=1
while cont<=10:
	print('{}-'.format(t), end='')
	t += r
	cont += 1
print('fim') 