from datetime import date
atual = date.today().year
ano=int(input('Ano de nascimento: '))
idade = atual-ano
print('O atleta tem {} anos'.format(idade))
if idade<9:
    print('Classificação: Mirim')
elif 9<=idade<14:
    print('Classificação: Infantil')
elif 14<=idade<19:
    print('Classificação: Junior')
elif 19<=idade<25:
    print('Classificação: Sênior')
else:
    print('Classificação: Master')