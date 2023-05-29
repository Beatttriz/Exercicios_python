primeiro=int(input('primeiro termo: '))
r=int(input('razão: '))
t=primeiro
cont=1
total=0
mais=10
while mais!=0:
	total=total+mais
	while cont<=total: 
	    print('{}-'.format(t), end='')
	    t+=r
	    cont += 1
	print('pausa')
	mais= int(input('Quantas mais quer saber? '))
print('acabou com {} termos mostrados'.format(total)) 