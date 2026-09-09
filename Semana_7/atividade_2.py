class Parada:
    def __init__(self, nome):
        self.nome = nome
        self.proximo = None
        self.anterior = None


class LinhaOnibus:
    def __init__(self):
        self.cabeca = None

    def adicionar_parada(self, nome):
        novo = Parada(nome)

        if self.cabeca is None:
            self.cabeca = novo
            novo.proximo = novo
            novo.anterior = novo
            return

        novo.proximo = self.cabeca
        novo.anterior = self.cabeca.anterior
        self.cabeca.anterior.proximo = novo
        self.cabeca.anterior = novo
        self.cabeca = novo

    def remover_parada(self):
        if self.cabeca is None:
            print("Lista vazia!")
            return

        alvo = input("Digite o nome da parada que deseja remover: ")
        atual = self.cabeca

        while True:
            if atual.nome == alvo:
                if atual == atual.proximo:
                    self.cabeca = None
                    print("Parada removida. Linha vazia.")
                    return

                if atual == self.cabeca:
                    self.cabeca = atual.proximo

                atual.anterior.proximo = atual.proximo
                atual.proximo.anterior = atual.anterior
                print("Parada removida com sucesso!")
                return

            if atual.proximo == self.cabeca:
                print("Parada nao encontrada!")
                return

            atual = atual.proximo

    def simular_percurso(self, total_paradas):
        if self.cabeca is None:
            print("Linha vazia, trajeto cancelado!")
            return

        atual = self.cabeca

        for etapa in range(1, total_paradas + 1):
            print("Parada", etapa, ":", atual.nome)
            atual = atual.proximo

    def listar(self):
        if self.cabeca is None:
            print("Lista vazia!")
            return

        atual = self.cabeca
        contador = 1

        while True:
            print(contador, "-", atual.nome)
            if atual.proximo == self.cabeca:
                return
            atual = atual.proximo
            contador += 1


linha = LinhaOnibus()
linha.adicionar_parada("Terminal Central")
linha.adicionar_parada("Hospital")
linha.adicionar_parada("Universidade")
linha.adicionar_parada("Praca Matriz")

print("--- Trajeto Cadastrado ---")
linha.listar()

print("\n--- Simulando Onibus em Movimento (8 paradas) ---")
linha.simular_percurso(8)

print("\n--- Removendo uma Parada ---")
linha.remover_parada()

print("\n--- Trajeto Atualizado ---")
linha.listar()
