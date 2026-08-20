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


def lista_altera(lst):
    atual = lst.inicio

    while atual is not None:
        atual.info = -atual.info
        atual = atual.proximo


def vizualizar(lst):
    atual = lst.inicio
    while atual is not None:
        print(atual.info, end=" -> ")
        atual = atual.proximo
    print("None")


lista = ListaEncadeada()

lista.inserir(10.0)
lista.inserir(-5.5)
lista.inserir(3.2)
lista.inserir(-8.0)

print("Antes da alteração:")
vizualizar(lista)

lista_altera(lista)

print("Depois da alteração:")
vizualizar(lista)