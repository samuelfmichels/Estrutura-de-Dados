import random
class Guerreiros:
    def __init__(self, guerreiros):
        self.guerreiros = guerreiros
        self.proximo = None
        self.anterior = None

class Lista:
    def __init__(self):
        self.cabeca = None

    def inserir(self, gurreiros):
        novo = Guerreiros(gurreiros)

        if self.cabeca == None:
            self.cabeca = novo
            novo.anterior = novo
            novo.proximo = novo
            return

        novo.proximo = self.cabeca
        novo.anterior = self.cabeca.anterior
        self.cabeca.anterior.proximo = novo
        self.cabeca.anterior = novo
        self.cabeca  = novo

    def jogar(self, total):
        if self.cabeca is None:
            print('Taverna vazia, guerreiro')
            return

        atual = self.cabeca

        while self.cabeca.proximo != self.cabeca:
            passos = random.randint(1, total)

            for i in range(passos):
                atual = atual.proximo

            print('Guerreiro eliminado: ', atual.guerreiros)

            if atual == self.cabeca:
                self.cabeca = atual.proximo

            atual.anterior.proximo = atual.proximo
            atual.proximo.anterior = atual.anterior

            atual = atual.proximo
            total -= 1
        print('Sobrevivente é: ', self.cabeca.guerreiros)


def main():
    taverna = Lista()
    total_guerreiros = 0       
    while True:
        print('Opção 1 - adicionar guerreiros')
        print('Opção 2 - fazer a simulação')
        opcao = int(input('Digite a opção que você deseja: '))
        if opcao == 1:
            for i in range(6):
                nome = input('Insira o nome do guerreiro ')
                taverna.inserir(nome)
                total_guerreiros = 6

        if opcao == 2:
            taverna.jogar(total_guerreiros)
            break

main()

                

    