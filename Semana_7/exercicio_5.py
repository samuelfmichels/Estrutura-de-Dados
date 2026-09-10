class Barracuda:
    def __init__(self, nome, idade, prioridade):
        self.nome = nome
        self.idade = idade
        self.prioridade = prioridade
        self.proximo = None
        self.anterior = None


class FilaHospital:
    def __init__(self):
        self.cabeca = None

    def inserir(self, nome, idade, prioridade):
        novo = Barracuda(nome, idade, prioridade)

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

    def remover_no(self, atual):
        if atual.proximo == atual:
            self.cabeca = None
            return

        if atual == self.cabeca:
            self.cabeca = atual.proximo

        atual.anterior.proximo = atual.proximo
        atual.proximo.anterior = atual.anterior

    def remover_atendido(self, nome):
        if self.cabeca == None:
            print("Fila vazia")
            return

        atual = self.cabeca

        while True:
            if atual.nome == nome:
                print("Paciente atendido e removido: ", atual.nome)
                self.remover_no(atual)
                return

            if atual.proximo == self.cabeca:
                print("Paciente nao encontrado")
                return

            atual = atual.proximo

    def mostrar(self):
        if self.cabeca == None:
            print("Fila vazia")
            return

        atual = self.cabeca

        while atual.proximo is not self.cabeca:
            print("Nome: ", atual.nome, " - Idade: ", atual.idade, " - Prioridade: ", atual.prioridade)
            atual = atual.proximo

        print("Nome: ", atual.nome, " - Idade: ", atual.idade, " - Prioridade: ", atual.prioridade)

    def simular_atendimento(self):
        if self.cabeca == None:
            print("Fila vazia")
            return

        ordem = ["emergencia", "urgente", "normal"]

        for prioridade_atual in ordem:
            while self.cabeca != None:
                achou = False
                atual = self.cabeca

                while True:
                    if atual.prioridade == prioridade_atual:
                        print("Atendendo agora: ", atual.nome, " - Prioridade: ", atual.prioridade)
                        self.remover_no(atual)
                        achou = True
                        break

                    if atual.proximo == self.cabeca:
                        break

                    atual = atual.proximo

                if achou == False:
                    break


def main():
    hospital = FilaHospital()

    while True:
        print("Opcao 1 - adicionar paciente")
        print("Opcao 2 - mostrar fila")
        print("Opcao 3 - remover paciente atendido")
        print("Opcao 4 - simular atendimento por prioridade")
        print("Opcao 5 - sair")
        opcao = int(input("Digite a opcao que voce deseja: "))

        if opcao == 1:
            nome = input("Insira o nome do paciente: ")
            idade = int(input("Insira a idade do paciente: "))
            prioridade = input("Insira a prioridade (emergencia, urgente, normal): ")
            hospital.inserir(nome, idade, prioridade)

        if opcao == 2:
            hospital.mostrar()

        if opcao == 3:
            nome = input("Insira o nome do paciente atendido para remover: ")
            hospital.remover_atendido(nome)

        if opcao == 4:
            hospital.simular_atendimento()

        if opcao == 5:
            break


main()
