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

    def inserir_fim(self, dado):
        novo = Node(dado)
        if self.fim is None:
            self.inicio = self.fim = novo
        else:
            novo.anterior = self.fim
            self.fim.proximo = novo
            self.fim = novo
        self.tamanho += 1

    def remover_inicio(self):
        if self.inicio is None:
            print("Fila vazia!")
            return
        atendido = self.inicio.dado
        self.inicio = self.inicio.proximo
        if self.inicio:
            self.inicio.anterior = None
        else:
            self.fim = None
        self.tamanho -= 1
        print("Atendido:", atendido)

    def listar(self):
        if self.inicio is None:
            print("Fila vazia!")
            return
        atual = self.inicio
        contador = 1
        print("Ordem de atendimento:")
        while atual is not None:
            print(contador, "- ", atual.dado)
            atual = atual.proximo
            contador += 1
        print()


def main():
    banco = Deque()

    while True:
        print("1 - Inserir cliente comum (fim)")
        print("2 - Inserir cliente preferencial (inicio)")
        print("3 - Atender cliente (inicio)")
        print("4 - Listar ordem de atendimento")
        print("5 - Sair")

        opcao = int(input("Digite a opcao: "))

        if opcao == 1:
            nome = input("Digite o nome: ")
            banco.inserir_fim(nome)
            banco.listar()

        elif opcao == 2:
            nome = input("Digite o nome: ")
            banco.inserir_inicio(nome)
            banco.listar()

        elif opcao == 3:
            banco.remover_inicio()
            banco.listar()

        elif opcao == 4:
            banco.listar()

        elif opcao == 5:
            print("Saindo...")
            break

        else:
            print("Vai toma no cu, Padilha")


main()
