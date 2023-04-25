primeiro=int(input('primeiro termo: '))
r=int(input('razão: '))
d=primeiro+(10-1)*r
for c in range (primeiro,d+r,r):
	print('{}'.format(c),end='-')
print('acabou') 