class Atleta:
    def __init__(self, atleta, id, situacao=False):
        self.atleta = atleta
        self.id = id
        self.situacao = situacao
        self.proximo = None
        self.anterior = Noneclass Listinha:
    def __init__(self):
        self.cabeca = None

    def inserir(self, atleta, id, situacao=False):
        novo = Atleta(atleta, id, situacao)

        if self.cabeca is None:
            novo.situacao = True
            self.cabeca = novo
            novo.proximo = novo
            novo.anterior = novo
            return

        novo.proximo = self.cabeca
        novo.anterior = self.cabeca.anterior
        self.cabeca.anterior.proximo = novo
        self.cabeca.anterior = novo
        self.cabeca = novo

    def remover(self):
        if self.cabeca is None:
            print("Lista vazia!")
            return

        atleta_alvo = input("Digite o atleta que deseja tirar: ")
        atual = self.cabeca

        while True:
            if atleta_alvo == atual.atleta:
                if atual.situacao == True:
                    atual.proximo.situacao = True

                if atual == atual.proximo:
                    self.cabeca = None
                    print("Atleta removido. Lista vazia.")
                    return

                if atual == self.cabeca:
                    self.cabeca = atual.proximo

                atual.anterior.proximo = atual.proximo
                atual.proximo.anterior = atual.anterior
                print("Atleta removido com sucesso!")
                return

            if atual.proximo == self.cabeca:
                print("Atleta não encontrado!")
                return

            atual = atual.proximo

    def passar_bastao(self, voltas):
        if self.cabeca is None:
            print("Lista vazia!")
            return

        atual = self.cabeca

        while atual.situacao != True:
            atual = atual.proximo

        for turno in range(1, voltas + 1):
            print("Turno", turno, "-", atual.atleta, "esta com o bastao.")
            atual.situacao = False
            atual = atual.proximo
            atual.situacao = True

    def listar(self):
        if self.cabeca is None:
            print("Lista vazia!")
            return

        atual = self.cabeca
        contador = 1

        while True:
            print(contador, "-", atual.atleta, "ID:", atual.id, " Bastao:", atual.situacao)
            if atual.proximo == self.cabeca:
                return
            atual = atual.proximo
            contador += 1


time = Listinha()
time.inserir("Carlos", 1)
time.inserir("Beatriz", 2)
time.inserir("Ana", 3)

print("Equipe inicial ")
time.listar()

print(" Simulando o revezamento")
time.passar_bastao(5)

print("- Situacao apos as passadas")
time.listar()

print(" Removendo atleta ")
time.remover()

print("Equipe final ")
time.listar()
