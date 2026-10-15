class Node:
    def __init__(self, dado):
        self.dado = dado
        self.proximo = None
        self.anterior = None


class Deque:
    def __init__(self):
        self.inicio = None
        self.fim = None
        self.tamanho = 0

    def inserir_inicio(self, dado):
        novo = Node(dado)
        if self.inicio is None:
            self.inicio = self.fim = novo
        else:
            novo.proximo = self.inicio
            self.inicio.anterior = novo
            self.inicio = novo
        self.tamanho += 1
        print("Chamado urgente", dado, "inserido no início")

    def inserir_fim(self, dado):
        novo = Node(dado)
        if self.fim is None:
            self.inicio = self.fim = novo
        else:
            novo.anterior = self.fim
            self.fim.proximo = novo
            self.fim = novo
        self.tamanho += 1
        print("Chamado comum", dado, "inserido no fim")

    def remover_inicio(self):
        if self.inicio is None:
            print("Deque vazio")
            return
        removido = self.inicio.dado
        self.inicio = self.inicio.proximo
        if self.inicio:
            self.inicio.anterior = None
        else:
            self.fim = None
        self.tamanho -= 1
        print("Chamado", removido, "atendido do início")

    def remover_fim(self):
        if self.fim is None:
            print("Deque vazio")
            return
        removido = self.fim.dado
        self.fim = self.fim.anterior
        if self.fim:
            self.fim.proximo = None
        else:
            self.inicio = None
        self.tamanho -= 1
        print("Chamado", removido, "atendido do fim")

    def listar_frente(self):
        if self.inicio is None:
            print("Deque vazio")
            return
        aux = self.inicio
        print("Chamados na fila (início -> fim):")
        while aux is not None:
            print("- ", aux.dado)
            aux = aux.proximo
        print()


def main():
    opcao = 0
    deque = Deque()
    while opcao != 6:
        print("1 - Adicionar chamado no fim da fila (chamado comum)")
        print("2 - Adicionar chamado no início da fila (chamado urgente)")
        print("3 - Atender chamado do início da fila (remoção do primeiro)")
        print("4 - Atender chamado do fim da fila (remoção do último)")
        print("5 - Listar todos os chamados da fila")
        print("6 - Sair do sistema")
        opcao = int(input("Qual a opção: "))

        if opcao == 1:
            dado = input("Descrição ou número do chamado comum: ")
            deque.inserir_fim(dado)
        elif opcao == 2:
            dado = input("Descrição ou número do chamado urgente: ")
            deque.inserir_inicio(dado)
        elif opcao == 3:
            deque.remover_inicio()
        elif opcao == 4:
            deque.remover_fim()
        elif opcao == 5:
            deque.listar_frente()


main()
