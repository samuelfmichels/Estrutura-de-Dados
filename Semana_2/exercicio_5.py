class No:
    def __init__(self, info):
        self.info = float(info)
        self.proximo = None


class ListaEncadeada:
    def __init__(self):
        self.inicio = None

    def inserir(self, info):
        novo = No(info)
        novo.proximo = self.inicio
        self.inicio = novo


def lista_calcula_media(lst):
    if lst.inicio is None:
        return 0.0

    soma = 0.0
    quantidade = 0
    atual = lst.inicio

    while atual is not None:
        soma += atual.info
        quantidade += 1
        atual = atual.proximo

    return soma / quantidade


lista = ListaEncadeada()

lista.inserir(10.0)
lista.inserir(20.0)
lista.inserir(30.0)

media = lista_calcula_media(lista)
print("Média dos valores:", media)