def aumentar(preço=0, taxa=0, formato=False):
    res=preço+(preço*taxa/100)
    return res if formato is False else teste(res)


def diminuir(preço=0, taxa=0, formato=False):
    res=preço-(preço*taxa/100)
    return res if formato is False else teste(res)


def dobro(preço=0, formato=False):
    res=preço*2
    return res if formato is False else teste(res)


def metade(preço=0, formato=False):
    res=preço/2
    return res if formato is False else teste(res)


def teste(preço=0, teste='R$'):
    return f'{teste}{preço:>.2f}'.replace('.',',')