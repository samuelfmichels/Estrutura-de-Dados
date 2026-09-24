class No:
    def __init__(self, nome):
        self.nome = nome
        self.proximo = None
        self.anterior = None

class Lista:
    def __init__(self):
        self.cabeca = None

    def inserir(self, nome):
        novo = No(nome)

        if self.cabeca == None:
            self.cabeca = novo
            return

        novo.proximo = self.cabeca
        self.cabeca.anterior = novo
        self.cabeca = novo
        return

    def listar(self):
        if self.cabeca == None:
            print('Lista vazia')

        atual = self.cabeca
        contador = 1

        while atual is not None:
            print(contador, ' - ', atual.nome)
            contador += 1
            atual = atual.proximo

        print('Lista completamente listada')

    def listar_inverso(self):
        if self.cabeca is None:
            print('Lista vazia')
        atual = self.cabeca
        contador = 1

        while atual.proximo is not None:
            atual = atual.proximo

        while atual is not None:
            print(contador, ' - ', atual.nome)
            atual = atual.anterior
            contador += 1

        print('Lista completamente corrida')

def main(listinha):
    while True:
        print('---Menu---')
        print('1 - Adicionar atleta')
        print('2 - Listar atleta')
        print('3 - Listar atletas na ordem inversa')
        opcao = int(input('Digite a opção: '))
        if opcao == 1:
            novo = input('Digite o nome do atleta: ')
            listinha.inserir(novo)
        elif opcao == 2:
            listinha.listar()
        elif opcao == 3:
            listinha.listar_inverso()
        else:
            print('Opcão incorreta!!!')

jogadores = Lista()
main(jogadores)