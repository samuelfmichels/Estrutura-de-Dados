class No:
    def __init__(self, info):
        self.info = int(info)
        self.proximo = None


class ListaEncadeada:
    def __init__(self):
        self.inicio = None

    def inserir(self, info):
        novo = No(info)
        novo.proximo = self.inicio
        self.inicio = novo


def maiores(lst, n):
    contador = 0
    atual = lst.inicio

    while atual is not None:
        if atual.info > n:
            contador += 1
        atual = atual.proximo

    return contador


lista = ListaEncadeada()

lista.inserir(15)
lista.inserir(3)
lista.inserir(20)
lista.inserir(8)
lista.inserir(50)

n = int(input("Digite o valor de n: "))
resultado = maiores(lista, n)
print("Quantidade de nós maiores que n:", resultado)