def aumentar(preço=0, taxa=0):
    res=preço+(preço*taxa/100)
    return res

def diminuir(preço=0, taxa=0):
    res=preço-(preço*taxa/100)
    return res

def dobro(preço=0):
    res=preço*2
    return res

def metade(preço=0):
    res=preço/2
    return res

def teste(preço=0, teste='R$'):
    return f'{teste}{preço:>.2f}'.replace('.',',')