print('aula1')
print('Olá.Mundo!')

print('aula2')
nome=input('Qual o seu nome?')
print('Olá! ',nome,' prazer em te conhecer!')

print('aula3')
n1=int(input('Digite um valor: '))
n2=int(input('Digite outro valor: '))
s=n1+n2
print('A soma entre {} e {} é igual a {}!'.format(n1, n2, s))

print('aula4')
a=input('Digite algo: ')
print('Tipo primitivo: ', type(a))
print('Tem apenas espaços: ',a.isspace())
print('É um número? ',a.isnumeric())
print('É alfabético? ', a.isalpha())
print('É alfanumérico? ',a.isalnum())
print('Está maiúsculo? ',a.isupper())
print('Está minúsculo? ', a.islower())
print('É capitalizada? ',a.istitle())


print('aula5')
n=int(input('Digite um número: '))
a=n-1
s=n+1
print('O valor é {}, seu antecessor é {} e o sucessor {}.'.format(n,a,s))

print('aula5pt2')
n=int(input('Digite um número: '))
print('O valor é {}, seu antecessor é {} e o sucessor {}. '.format(n,(n-1),(n+1)))

print('aula6')
n=int(input('Digite um número: '))
d=n*2
t=n*3
r=n**(1/2)
print('O dobro de {} é {}, já o seu triplo é {}, sua raiz {}.'.format(n,d,t,r))

print('aula6pt2')
n=int(input('Digite um número: '))
print('O dobro de {} é {}, já o seu triplo é {}, sua raiz {}.'.format(n,(n*2),(n*3),(n**(1/2))))

print('aula7')
n1=float(input('Primeira nota: '))
n2=float(input('Segunda nota: '))
media=(n1+n2)/2
print('A média entre {} e {} é {}'.format(n1,n2,media))

print('aula8')
media=float(input('Distância em metros: '))
cm=media*100
mm=media*1000
print('A medida de {} em centímetros é {} e em milímetros {}'.format(media,cm,mm))

num=int(input('Digite um número para ver sua tabuada: '))
print('-'*12)
print('{} x {:2} = {}'.format(num, 1, num*1))
print('{} x {:2} = {}'.format(num, 2, num*2))
print('{} x {:2} = {}'.format(num, 3, num*3))
print('{} x {:2} = {}'.format(num, 4, num*4))
print('{} x {:2} = {}'.format(num, 5, num*5))
print('{} x {:2} = {}'.format(num, 6, num*6))
print('{} x {:2} = {}'.format(num, 7, num*7))
print('{} x {:2} = {}'.format(num, 8, num*8))
print('{} x {:2} = {}'.format(num, 9, num*9))
print('{} x {:2} = {}'.format(num, 10, num*10))
print('-'*12)

print('Desafio 10')
real=float(input('Quanto dinheiro? R$'))
dolar=real/5.45
print('Com R${:.2f} você pode comprar US${:.2f}'.format(real,dolar))

print('Desafio 11')
larg=float(input('Largura da parede: '))
alt=float(input('Altura: '))
area=larg*alt
tinta=area/2
print('Você precisa de {}l de tinta.'.format(tinta))

print('Desafio 12')
preço=float(input('Qual é o preço do produto? R$'))
novo=preço-(preço*5/100)
print('Custa com 5% de desconto R${:.2f}'.format(novo))

print('Desafio 13')
salario=float(input('Seu salário atual R$'))
novo=salario+(salario*15/100)
print('Depois do aumento R${:.2f}'.format(novo))

print('Desafio 14')
c=float(input('Temperatura em ºC'))
f=9*c/5+32
print('A temperatura em ºF é {}ºF'.format(f))

print('Desafio 15')
dias=int(input('Quantos dias alugados? '))
km=float(input('Quantos km rodados?'))
pago=(dias*60)+(km*0.15)
print('Pagar R${:.2f}'.format(pago))

from math import trunc
num=float(input('valor: '))
print('a porção inteira do valor digitado é {}'.format(trunc(num)))

print('desafio17')
from math import hypot
co=float(input('Cateto oposto: '))
ca=float(input('Cateto adjacente: '))
hi=hypot(co,ca)
print('A hipotenusa vai medir {:.2f}'.format(hi))

print('desafio18')
from math import radians, sin, cos, tan
an=float(input('Angulo '))
seno=sin(radians(an))
print('angulo de {} tem o seno de {:.2f}'.format(an,seno))
cosseno=cos(radians(an))
print('angulo de {} tem cosseno de {:.2f}'.format(an,cosseno))
tangente=tan(radians(an))
print('angulo de {} tem a tangente de {:.2f}'.format(an, tangente))

print('desafio19')
from random import choice
n1 = str(input('Primeiro nome'))
n2 = str(input('Segundo nome'))
n3 = str(input('Terceiroo nome'))
n4 = str(input('Quarto nome'))
lista=[n1,n2,n3,n4]
escolhido=choice(lista)
print('O aluno escolhido foi {}'.format(escolhido))

print('desafio20')
from random import shuffle
n1 = str(input('Primeiro nome'))
n2 = str(input('Segundo nome'))
n3 = str(input('Terceiroo nome'))
n4 = str(input('Quarto nome'))
lista=[n1,n2,n3,n4]
shuffle(lista)
print('a ordem é')
print(lista)

print('desafio22')
nome = str(input('Digite um nome completo: ')).strip()
print('analisando seu nome...')
print('seu nome em maiúsculas é {}'.format(nome.upper()))
print('seu nome em minúsculas é {}'.format(nome.lower()))
print('seu nome ao todo tem {} letras'.format(len(nome) - nome.count(' ')))
# print('seu primeiro nome tem {} letras'.format(nome.find('')))
separa = nome.split()
print('seu primeiro nome é {} e ele tem {} letras'.format(separa[0], len(separa[0])))

print('desafio23')
num = int(input('informe um número: '))
u = num//1 % 10
d = num//10 % 10
c = num//100 % 10
m = num//1000 % 10
print('analisando número {}'.format(num))
print('unidade: {}'.format(u))
print('dezena: {}'.format(d))
print('centena: {}'.format(c))
print('milhar: {}'.format(m))

print('desafio24')
cid = str(input('em que cidade você nasceu?')).strip()
print(cid[:5].upper() == 'SANTO')

print('desafio25')
nome = str(input('qual seu nome completo?')).strip()
print('seu nome  tem silva? {}'.format('silva' in nome.lower()))

print('desafio26')
frase = str(input('digite uma frase: ')).upper().strip()
print('a letra a aparece{} vezes na frase.'.format(frase.count('A')))
print('a primeira letra a apareceu na posição {}.'.format(frase.find('A')+1))
print('a última letra a apareceu na posição {}.'.format(frase.rfind('A')+1))

print('desafio27')
n = str(input('digite seu nome completo')).strip()
nome = n.split()
print('seu primeiro nome é {}'.format(nome[0]))
print('seu último nome é {}'.format(nome[len(nome)-1]))

print('desafio28')
from random import randint
from time import sleep
computador = randint(0, 5)
print('-=-'*20)
print('vou pensar em um número entre 0 e 5...')
print('-=-'*20)
jogador=int(input('em que número eu pensei? '))
sleep(3)
if jogador == computador:
    print('você venceu')
else:
    print('você perdeu, eu pensei no {}'.format(computador))

print('desafio29')
velocidade = float(input('qual é a velocidade atual do carro?'))
if velocidade > 80:
    print('multado, o limite de velocidade é 80km')
    multa= (velocidade-80) * 7
    print('sua multa vai custar R${:.2f}:'.format(multa))
else:
    print('dirija com segurança')

print('desafio30')
n=int(input('me fala um número: '))
resultado= n % 2
if resultado == 0:
    print('o número é par')
else:
    print('é ímpar')

print('desafio31')
d=float(input('qual a distância? '))
preço=d * 0.50 if d <= 200 else d * 0.45
print('valor da passagem R${:.2}' .format(preço))

print('desafio32')
ano = int(input('que ano quer analisar?'))
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 ==0 :
    print('o ano é bissexto')
else:
    print('não é bissexto')

print('desafio33')
a=int(input('primeiro valor: '))
b=int(input('segundo valor: '))
c=int(input('terceiro valor: '))
menor=a
if b<a and b<c:
    menor = b
if c<a and c<b:
    menor = c
maior = a
if b>a and b>c:
    maior = b
if c>a and c>b:
    maior = c
print('menor {}'.format(menor))
print('maior {}'.format(maior))

print('desafio34')
s=float(input('salário: '))
if s <= 1250:
    novo= s+(s* 15/100)
else:
    novo = s + (s * 10 / 100)
print('seu novo sálario é {}'.format(novo))

print('desafio35')
r1=float(input('primeiro segmento'))
r2=float(input('segundo segmento'))
r3=float(input('terceiro segmento'))
if r1<r2+r3 and r2<r1+r3 and r3<r1+r2:
    print('podem formar um triângulo')
else:
    print('não podem formar um triângulo')

print('aula12')
nome = str(input('Nome?'))
if nome == 'Bia':
    print('nome lindo')
elif nome == 'Pedro' or nome == 'Tiago' or nome == 'João':
    print('nome comum')
elif nome in 'Ana Maria':
    print('nome feminino comum')
else:
    print('Bem normal esse nome')
print('Bom dia, {}'.format(nome))

print('desafio36')
casa = float(input('Valor da casa: R$'))
sal = float(input('Salário do comprador: R$'))
anos = int(input('Quantos anos de financiamento?'))
prest = casa/(anos*12)
min = sal *30/100
print('Para pagar a casa de R$ {:.2f} em {} anos'.format(casa,anos), end='')
print(' A prestação será de R${:.2f}'.format(prest))
if prest <= min:
    print('Concedido')
else:
    print('Negado')

print('desafio38')
n1=int(input('Primeiro'))
n2=int(input('Segundo'))
if n1>n2:
    print('O primeiro é maior')
elif n1<n2:
    print('O segundo é maior')
else:
    print('os dois são iguais')
    
print('desafio39')
from datetime import date
atual = date.today().year
nasc = int(input('Ano de nascimento: '))
idade = atual - nasc
print('Quem nasceu em {} tem {} anos em {}.'.format(nasc, idade, atual))
if idade == 18:
    print('Você tem que se alistar')
elif idade < 18:
    saldo = 18 - idade
    print('Aimda falta {} anos para seu alistamento'.format(saldo))
    ano = atual + saldo
    print('Seua alistamento será em {}'.format(ano))
elif idade > 18:
    saldo = idade -18
    print('Você já deveria ter se alistado há {} anos '.format(saldo))
    ano= atual - saldo
    print('Seu alistamento foi em {}'.format(ano))


