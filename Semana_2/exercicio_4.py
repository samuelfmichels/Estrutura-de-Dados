class No:
    def __init__(self, info):
        self.info = info
        self.proximo = None


class ListaEncadeada:
    def __init__(self):
        self.inicio = None


def lista_insere_final(lst, valor):
    novo = No(valor)

    if lst.inicio is None:
        lst.inicio = novo
        return

    atual = lst.inicio
    while atual.proximo is not None:
        atual = atual.proximo

    atual.proximo = novo


def vizualizar(lst):
    atual = lst.inicio
    while atual is not None:
        print(atual.info, end=" -> ")
        atual = atual.proximo
    print("None")


lista = ListaEncadeada()

lista_insere_final(lista, 10)
lista_insere_final(lista, 20)
lista_insere_final(lista, 30)

vizualizar(lista)