class Barracuda:
    def __init__(self, nome):
        self.nome = nome
        self.proximo = None
        self.anterior = None


class Rodizio:
    def __init__(self):
        self.cabeca = None

    def inserir(self, nome):
        novo = Barracuda(nome)

        if self.cabeca == None:
            novo.proximo = novo
            novo.anterior = novo
            self.cabeca = novo
            return

        novo.proximo = self.cabeca
        novo.anterior = self.cabeca.anterior
        self.cabeca.anterior.proximo = novo
        self.cabeca.anterior = novo
        self.cabeca = novo

    def exclusao(self, nome):
        if self.cabeca == None:
            print("Lista vazia")
            return

        atual = self.cabeca

        while True:
            if atual.nome == nome:
                if atual.proximo == atual:
                    self.cabeca = None
                    print("Cliente removido, mesa vazia")
                    return

                if atual == self.cabeca:
                    self.cabeca = atual.proximo

                atual.anterior.proximo = atual.proximo
                atual.proximo.anterior = atual.anterior
                print("Cliente removido com sucesso")
                return

            if atual.proximo == self.cabeca:
                print("Cliente nao encontrado")
                return

            atual = atual.proximo

    def rodizio(self):
        if self.cabeca == None:
            print("Lista vazia")
            return

        atual = self.cabeca

        while atual.proximo is not self.cabeca:
            print("Quem esta recebendo a fatia e: ", atual.nome)
            atual = atual.proximo

        print("Quem esta recebendo a fatia e: ", atual.nome)


def main():
    mesa = Rodizio()

    while True:
        print("Opcao 1 - adicionar cliente")
        print("Opcao 2 - passar pizza")
        print("Opcao 3 - retirar cliente")
        print("Opcao 4 - sair")
        opcao = int(input("Digite a opcao que voce deseja: "))

        if opcao == 1:
            nome = input("Insira o nome do cliente: ")
            mesa.inserir(nome)

        if opcao == 2:
            mesa.rodizio()

        if opcao == 3:
            nome = input("Digite o nome do cliente para remover: ")
            mesa.exclusao(nome)

        if opcao == 4:
            break


main()