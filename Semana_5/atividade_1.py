class Barracuda:
    def __init__(self, matricula, nome, nota):
        self.matricula = matricula
        self.nome = nome
        self.situacao = True
        self.nota = nota
        self.proximo = None


class Turma:
    def __init__(self):
        self.cabeca = None

    def cadastrar_turma(self, matricula, nome, nota):
        novo = Barracuda(matricula, nome, nota)

        if self.cabeca is None:
            self.cabeca = novo
            return

        atual = self.cabeca
        while atual.proximo is not None:
            atual = atual.proximo
        atual.proximo = novo

    def listar_alunos(self):
        if self.cabeca is None:
            print('Turma sem alunos, sinto muito')
            return

        atual = self.cabeca
        while atual is not None:
            print('Nome: ', atual.nome)
            print('Matricula: ', atual.matricula)
            atual = atual.proximo

    def alunos_ativos(self):
        if self.cabeca is None:
            print('Turma vazia')
            return

        print('Alunos ativos: ')
        atual = self.cabeca
        while atual is not None:
            if atual.situacao is True:
                print('Nome: ', atual.nome)
            atual = atual.proximo

    def alunos_desativados(self):
        if self.cabeca is None:
            print('Turma vazia')
            return

        print('Alunos desativados: ')
        atual = self.cabeca
        while atual is not None:
            if atual.situacao is False:
                print('Nome: ', atual.nome)
            atual = atual.proximo

    def busca_matricula(self):
        if self.cabeca is None:
            print('Turma vazia')
            return

        matricula = int(input('Digite a matricula que deseja buscar: '))
        atual = self.cabeca
        while atual is not None:
            if matricula == atual.matricula:
                print('Nome: ', atual.nome)
                print('Matricula: ', atual.matricula)
                print('Nota: ', atual.nota)
                print('Situação: ', atual.situacao)
                return
            atual = atual.proximo
        print('Aluno não encontrado.')

    def alterar_nota(self):
        if self.cabeca is None:
            print('Turma vazia')
            return

        matricula = int(input('Digite a matricula: '))
        atual = self.cabeca
        while atual is not None:
            if atual.matricula == matricula:
                notinha = float(input('Digite a nota que deve ser corrigida: '))
                print('Nota antiga: ', atual.nota)
                atual.nota = notinha
                print('Nova nota: ', atual.nota)
                return
            atual = atual.proximo
        print('Aluno não encontrado.')

    def alterar_situacao(self):
        if self.cabeca is None:
            print('Turma vazia')
            return

        matricula = int(input('Digite a Matricula: '))
        atual = self.cabeca

        while atual is not None:
            if atual.matricula == matricula:
                atual.situacao = not atual.situacao
                print('Situação alterada')
                return
            atual = atual.proximo
        print('Aluno não encontrado.')

    def remover_aluno(self):
        if self.cabeca is None:
            print('Turma vazia')
            return

        matricula = int(input('Digite a Matricula: '))
        atual = self.cabeca
        anterior = None

        while atual is not None:
            if atual.matricula == matricula:
                print('Aluno removido: ', atual.nome)
                if anterior is None:
                    self.cabeca = atual.proximo
                else:
                    anterior.proximo = atual.proximo
                return

            anterior = atual
            atual = atual.proximo
        print('Aluno não encontrado.')

    def quantidade_alunos(self):
        quantidade = 0
        atual = self.cabeca
        while atual is not None:
            quantidade += 1
            atual = atual.proximo
        print('Quantidade de alunos cadastrados: ', quantidade)
        return quantidade

    def media_turma(self):
        if self.cabeca is None:
            print('Turma vazia')
            return 0.0

        soma = 0
        quantidade = 0
        atual = self.cabeca
        while atual is not None:
            soma += atual.nota
            quantidade += 1
            atual = atual.proximo

        media = soma / quantidade
        print('Média das notas da turma: ', media)
        return media

    def media_alunos_ativos(self):
        if self.cabeca is None:
            print('Turma vazia')
            return 0.0

        soma = 0
        quantidade = 0
        atual = self.cabeca
        while atual is not None:
            if atual.situacao is True:
                soma += atual.nota
                quantidade += 1
            atual = atual.proximo

        if quantidade == 0:
            print('Nenhum aluno ativo na turma')
            return 0.0

        media = soma / quantidade
        print('Média das notas dos alunos ativos: ', media)
        return media



turma = Turma()

turma.cadastrar_turma(101, 'Lucas', 8.5)
turma.cadastrar_turma(102, 'Mariana', 9.0)
turma.cadastrar_turma(103, 'Carlos', 5.5)

turma = Turma()

while True:
    print("\n--- MENU TURMA ---")
    print("1. Cadastrar aluno no final")
    print("2. Listar todos os alunos")
    print("3. Listar apenas alunos ativos")
    print("4. Listar apenas alunos desativados")
    print("5. Buscar aluno por matrícula")
    print("6. Alterar nota final")
    print("7. Alterar situação do aluno")
    print("8. Remover aluno")
    print("9. Quantidade de alunos cadastrados")
    print("10. Média das notas da turma")
    print("11. Média das notas dos alunos ativos")
    print("0. Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == '1':
        mat = int(input("Digite a matrícula: "))
        nome = input("Digite o nome: ")
        nota = float(input("Digite a nota final: "))
        turma.cadastrar_turma(mat, nome, nota)
        print("Aluno cadastrado com sucesso!")
    elif opcao == '2':
        turma.listar_alunos()
    elif opcao == '3':
        turma.alunos_ativos()
    elif opcao == '4':
        turma.alunos_desativados()
    elif opcao == '5':
        turma.busca_matricula()
    elif opcao == '6':
        turma.alterar_nota()
    elif opcao == '7':
        turma.alterar_situacao()
    elif opcao == '8':
        turma.remover_aluno()
    elif opcao == '9':
        turma.quantidade_alunos()
    elif opcao == '10':
        turma.media_turma()
    elif opcao == '11':
        turma.media_alunos_ativos()
    elif opcao == '0':
        break
    else:
        print("Opção inválida, tente novamente.")
