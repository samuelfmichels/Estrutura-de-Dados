class No:
    def __init__(self, nome, gols):
        self.nome = nome
        self.gols = gols
        self.proximo = None

class Lista:
    def __init__(self):
        self.cabeca = None

    def inserir(self, nome, gols):
        novo = No(nome, gols)
        novo.proximo = self.cabeca
        self.cabeca = novo

    def inserir_fim(self, nome, gols):
        novo = No(nome, gols)

        if self.cabeca is None:
            self.cabeca = novo
            return

        atual = self.cabeca
        while atual.proximo is not None:
            atual = atual.proximo

        atual.proximo = novo
        
    def listar(self):
        if self.cabeca is None:
            print('Lista vazia')
            return
        atual = self.cabeca
        contador = 1
        while atual is not None:
            print(contador, ' - ', atual.nome, '| número de gols: ', atual.gols )
            contador += 1
            atual = atual.proximo

        print('Lista completamente percorrida')

def main(listinha):
    while True:
        print('---Lista de Jogadores---')
        print('1 - inserir jogadores')
        print('2 - listar jogadores')
        print('3 - inserir fim')
        print('4 - sair')

        opcao = int(input('Digite a opcão: '))

        if opcao == 1:
            novo = input('Insira o nome do jogador: ')
            gols = int(input('Insira a quantidade de gols: '))
            listinha.inserir(novo, gols)
        elif opcao == 2:
            listinha.listar()
        elif opcao == 3:
            novo = input('Insira o nome do jogador: ')
            gols = int(input('Insira a quantidade de gols: '))
            listinha.inserir_fim(novo, gols)
        elif opcao == 4:
            print('Saindo')
            break
        else:
            print('Tente novamente! ')

jogadores = Lista()
main(jogadores)
