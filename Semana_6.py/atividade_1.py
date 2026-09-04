class Barracuda:
    def __init__(self, id, situacao=False):
        self.id = id
        self.situacao = situacao
        self.proximo = None
        self.anterior = None

def inserir(lista, id):
    primeiro = lista is None
    no = Barracuda(id, primeiro)

    if lista is None:
        no.proximo = no
        no.anterior = no
        lista = no
        return lista

    no.proximo = lista
    no.anterior = lista.anterior
    lista.anterior.proximo = no
    lista.anterior = no
    lista = no
    return lista

def excluir(lista, id):
    atual = lista

    if lista is None:
        print('Lista vazia')
        return lista

    while True:
        if atual.id == id:
            if atual.situacao and atual.proximo != atual:
                atual.proximo.situacao = True

            if atual.proximo == atual:
                print('Único elemento da lista')
                return None
            elif atual == lista:
                lista.proximo.anterior = lista.anterior
                lista.anterior.proximo = lista.proximo
                lista = lista.proximo
                return lista
            else:
                atual.proximo.anterior = atual.anterior
                atual.anterior.proximo = atual.proximo
                return lista

        elif atual.proximo == lista:
            print('Dado não encontrado')
            return lista
        atual = atual.proximo

def listar(lista):
    atual = lista

    if lista is None:
        print('A lista está vazia')
        return

    while True:
        print('Id:', atual.id)
        if atual.situacao:
            print('- Está com o bastão')
        else:
            print('- Não está com o bastão')

        if atual.proximo == lista:
            return
        atual = atual.proximo

def simular(lista, rodadas):
    if lista is None:
        print('A lista está vazia')
        return

    atual = lista
    while not atual.situacao:
        atual = atual.proximo

    for i in range(rodadas):
        print('Turno:', i + 1)
        print('Atleta', atual.id, 'passou o bastão para o atleta', atual.proximo.id)
        atual.situacao = False
        atual = atual.proximo
        atual.situacao = True
        print('Atleta com o bastão agora:', atual.id)

jogadores = None
jogadores = inserir(jogadores, 1)
jogadores = inserir(jogadores, 2)
jogadores = inserir(jogadores, 3)

listar(jogadores)
simular(jogadores, 3)
