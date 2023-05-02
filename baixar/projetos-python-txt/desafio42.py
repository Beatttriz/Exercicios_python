s1=int(input('Primeiro segmento: '))
s2=int(input('Segundo segmento: '))
s3=int(input('Terceiro segmento: '))
if s1<s2+s3 and s2<s1+s3 and s3<s1+s2:
    print('Podem formar um triângulo')
    if s1 == s2 == s3:
        print('equilátero')
    elif s1 != s2 != s3 != s1:
        print('escaleno')
    else:
        print('isósceles') 
else:
    print('Não podem formar um triângulo')