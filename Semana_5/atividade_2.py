class Paciente:
    def __init__(self, id_paciente, nome, prioridade):
        self.id = id_paciente
        self.nome = nome
        self.prioridade = prioridade
        self.proximo = None
        self.anterior = None


class FilaClinica:
    def __init__(self):
        self.cabeca = None
        self.cauda = None

    def inserir_fim(self):
        id_p = int(input("Digite o ID do paciente: "))
        nome = input("Digite o nome: ")
        prioridade = input("Digite a prioridade (Normal/Urgente): ")
        novo = Paciente(id_p, nome, prioridade)

        if self.cabeca is None:
            self.cabeca = novo
            self.cauda = novo
            print("Paciente adicionado com sucesso!")
            return

        self.cauda.proximo = novo
        novo.anterior = self.cauda
        self.cauda = novo
        print("Paciente adicionado ao fim da fila!")

    def inserir_inicio(self):
        id_p = int(input("Digite o ID do paciente: "))
        nome = input("Digite o nome: ")
        prioridade = input("Digite a prioridade (Normal/Urgente): ")
        novo = Paciente(id_p, nome, prioridade)

        if self.cabeca is None:
            self.cabeca = novo
            self.cauda = novo
            print("Paciente adicionado com sucesso!")
            return

        novo.proximo = self.cabeca
        self.cabeca.anterior = novo
        self.cabeca = novo
        print("Paciente adicionado no início da fila!")

    def listar_ordem(self):
        if self.cabeca is None:
            print("Fila vazia")
            return

        print("Fila de Atendimento:")
        atual = self.cabeca
        while atual is not None:
            print("ID: ", atual.id)
            print("Nome: ", atual.nome)
            print("Prioridade: ", atual.prioridade)
            atual = atual.proximo

    def listar_ordem_inversa(self):
        if self.cauda is None:
            print("Fila vazia")
            return

        print("Fila do Fim ao Início:")
        atual = self.cauda
        while atual is not None:
            print("ID: ", atual.id)
            print("Nome: ", atual.nome)
            print("Prioridade: ", atual.prioridade)
            atual = atual.anterior

    def atender_proximo(self):
        if self.cabeca is None:
            print("Nenhum paciente na fila")
            return

        atendido = self.cabeca
        print("Atendendo paciente: ", atendido.nome)

        if self.cabeca == self.cauda:
            self.cabeca = None
            self.cauda = None
            return

        self.cabeca = self.cabeca.proximo
        self.cabeca.anterior = None

    def buscar_paciente(self):
        if self.cabeca is None:
            print("Fila vazia")
            return

        id_busca = int(input("Digite o ID que deseja buscar: "))
        atual = self.cabeca
        posicao = 1
        while atual is not None:
            if atual.id == id_busca:
                print("Paciente encontrado na posição: ", posicao)
                print("Nome: ", atual.nome)
                print("ID: ", atual.id)
                print("Prioridade: ", atual.prioridade)
                return
            atual = atual.proximo
            posicao += 1
        print("Paciente não encontrado")

    def desistir_atendimento(self):
        if self.cabeca is None:
            print("Fila vazia")
            return

        id_busca = int(input("Digite o ID do paciente desistente: "))
        atual = self.cabeca

        while atual is not None:
            if atual.id == id_busca:
                print("Paciente removido: ", atual.nome)
                if atual == self.cabeca and atual == self.cauda:
                    self.cabeca = None
                    self.cauda = None
                elif atual == self.cabeca:
                    self.cabeca = self.cabeca.proximo
                    self.cabeca.anterior = None
                elif atual == self.cauda:
                    self.cauda = self.cauda.anterior
                    self.cauda.proximo = None
                else:
                    atual.anterior.proximo = atual.proximo
                    atual.proximo.anterior = atual.anterior
                return
            atual = atual.proximo

        print("Paciente não encontrado")

    def total_pacientes(self):
        total = 0
        atual = self.cabeca
        while atual is not None:
            total += 1
            atual = atual.proximo
        print("Total de pacientes na fila: ", total)
        return total


fila = FilaClinica()

while True:
    print("\n--- MENU CLINICA ---")
    print("1. Inserir paciente no fim da fila")
    print("2. Inserir paciente no inicio da fila")
    print("3. Atender proximo paciente")
    print("4. Listar fila do inicio ao fim")
    print("5. Listar fila do fim ao inicio")
    print("6. Buscar paciente por ID")
    print("7. Remover paciente por desistencia")
    print("8. Ver total de pacientes na fila")
    print("0. Sair")

    opcao = input("Escolha uma opcao: ")

    if opcao == '1':
        fila.inserir_fim()
    elif opcao == '2':
        fila.inserir_inicio()
    elif opcao == '3':
        fila.atender_proximo()
    elif opcao == '4':
        fila.listar_ordem()
    elif opcao == '5':
        fila.listar_ordem_inversa()
    elif opcao == '6':
        fila.buscar_paciente()
    elif opcao == '7':
        fila.desistir_atendimento()
    elif opcao == '8':
        fila.total_pacientes()
    elif opcao == '0':
        break
    else:
        print("Opcao invalida, tente novamente.")