from math import radians, sin, cos, tan
an=float(input('Angulo '))
seno=sin(radians(an))
print('angulo de {} tem o seno de {:.2f}'.format(an,seno))
cosseno=cos(radians(an))
print('angulo de {} tem cosseno de {:.2f}'.format(an,cosseno))
tangente=tan(radians(an))
print('angulo de {} tem a tangente de {:.2f}'.format(an, tangente))