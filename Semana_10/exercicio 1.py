class Barracuda:
    def __init__(self, nome, responsavel):
        self.nome = nome
        self.responsavel = responsavel
        self.proximo = None


class Lista:
    def __init__(self):
        self.cabeca = None

    def inserir(self, nome, responsavel):
        novo = Barracuda(nome, responsavel)
        novo.proximo = self.cabeca
        self.cabeca = novo
      
    def listar(self):
        if self.cabeca == None:
            print("Lista vazia!")
            return

        atual = self.cabeca
        contador = 1
        while atual is not None:
            print(contador, "- ", atual.nome, atual.responsavel)
            atual = atual.proximo
            contador += 1

    def excluir(self, alvo):
        if self.cabeca == None:
            print("Lista vazia!")
            return

        if self.cabeca.nome == alvo:
            self.cabeca = self.cabeca.proximo
            return

        atual = self.cabeca
        anterior = None
        while atual is not None:
            if atual.nome == alvo:
                anterior.proximo = atual.proximo
                return
            anterior = atual
            atual = atual.proximo

        print("Alvo não encontrado!")


def main():
    jogadores = Lista()

    jogadores.inserir("Planejamento do Produto", "Ana")
    jogadores.inserir("Implementação do Backend", "João")
    jogadores.inserir("Testes Automatizados", "Carla")

    jogadores.listar()

    jogadores.excluir("Planejamento do Produto")

    jogadores.listar()


main()
