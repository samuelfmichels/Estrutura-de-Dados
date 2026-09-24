class Barracuda:
    def __init__(self, dado):
        self.dado = dado
        self.proximo = None
        self.anterior = None

class Listinha:
    def __init__(self):
        self.cabeca = None

    def inserir_dado(self, dado):
        novo = Barracuda(dado)

        if self.cabeca == None:
            self.cabeca = novo 
            self.cabeca.anterior = novo
            self.cabeca.proximo = novo
            return

        novo.proximo = self.cabeca
        novo.anterior = self.cabeca.anterior
        self.cabeca.anterior.proximo = novo
        self.cabeca.anterior = novo
        self.cabeca = novo
        return

    def inserir_fim(self, dado):
        novo = Barracuda(dado)

        if self.cabeca == None:
            self.cabeca = novo
            self.cabeca.proximo = self.cabeca
            self.cabeca.anterior = self.cabeca
            return

        novo.proximo = self.cabeca
        novo.anterior = self.cabeca.anterior
        self.cabeca.anterior.proximo = novo
        self.cabeca.anterior = novo
        return

    def listar_frente(self, quantidade):
        if self.cabeca == None:
            print('Lista vazia! ')
            return

        atual = self.cabeca
        contador = 0
        contador_1 = 1


        while contador != quantidade:
            print(contador_1, ' - ', atual.dado)
            contador_1 += 1

            atual = atual.proximo
            if atual == self.cabeca:
                contador += 1

        print('Lista completamente percorrida ', quantidade,' vezes! ')


    def percorrer_atras(self, quantidade):
        if self.cabeca == None:
            print('Lista vazia! ')

        atual = self.cabeca.anterior
        contador = 0
        contador_1 = 1

        while contador != quantidade:
            print(contador_1, ' - ', atual.dado)
            contador_1 += 1
            atual = atual.anterior
            if atual == self.cabeca.anterior:
                contador += 1

        print('Lista percorrida ', quantidade, 'vezes')


    def excluir_cabeca(self):
        if self.cabeca == None:
            print('Lista vazia!')

        if self.cabeca.proximo == self.cabeca:
            self.cabeca.proximo = None
            self.cabeca.anterior = None
            self.cabeca = None
            return


        self.cabeca.anterior.proximo = self.cabeca.proximo
        self.cabeca.proximo.anterior = self.cabeca.anterior
        self.cabeca = self.cabeca.proximo
        
def main():
    jogadores = Listinha()

    while True:
        print('1 - Inserir')
        print('2 - Inserir fim')
        print('3 - Lista')
        print('4 - Lista inverso')
        print('5 - Excluir')

        opcao = int(input('Digite a opção desejada: '))
        if opcao == 1:
            novo = int(input('Digite um número a ser adicionado: '))
            jogadores.inserir_dado(novo)

        elif opcao == 2:
            novo = int(input('Digite um número a ser adicionado: '))
            jogadores.inserir_fim(novo)

        elif opcao == 3:
            quantidade = int(input('Digite a quantidade de vezes que a lista ira percorrer'))
            jogadores.listar_frente(quantidade)

        elif opcao == 4:
            quantidade = int(input('Digite a quantidade de vezes que a lista ira percorrer'))
            jogadores.percorrer_atras(quantidade)

        elif opcao == 5:
            jogadores.excluir_cabeca()

        elif opcao == 6:
            print('Saindo...')
            break

        else:
            print('Vai toma no cu, Padilha')

main()