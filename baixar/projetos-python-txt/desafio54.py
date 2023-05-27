cont = 0
from datetime import date
atual = date.today().year
for c in range (0, 7):
    idade = int(input('Em que ano você nasceu?'))
    if atual - idade >=21:
        cont += 1
        restante = 7 - cont
print('{} pessoas já são maiores de idade e {} pessoas ainda não são' .format(cont, restante))
'''copiei cod de comentário'''