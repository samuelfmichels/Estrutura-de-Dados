class No:
    def __init__(self, nome):
        self.nome = nome
        self.proximo = None

class Fila:
    def __init__(self):
        self.inicio = None
        self.fim = None

def adicionar_jogador(fila, nome):
    novo = No(nome)
    if fila.inicio is None:
        fila.inicio = novo
        fila.fim = novo
    else:
        fila.fim.proximo = novo
        fila.fim = novo

def simular_rodada(fila):
    if fila.inicio is None:
        print('Fila vazia, meu amiguinho')
        return

    if fila.inicio == fila.fim:
        print('Jogador atual:', fila.inicio.nome)
        return

    jogou = fila.inicio
    fila.inicio = fila.inicio.proximo

    jogou.proximo = None
    fila.fim.proximo = jogou
    fila.fim = jogou

    print('Quem jogou nesta rodada:', jogou.nome)

def simular_n_rodadas(fila, n):
    for i in range(n):
        print('--- Rodada', i + 1, '---')
        simular_rodada(fila)
        mostrar_fila(fila)

def mostrar_fila(fila):
    if fila.inicio is None:
        print('Fila vazia!')
        return

    atual = fila.inicio
    contador = 1
    print('--- CARROS NA FILA ---')
    while atual is not None:
        print(contador, '-', atual.nome)
        atual = atual.proximo
        contador += 1

def proximo_jogar(fila):
    if fila.inicio is None:
        print('Fila vazia!')
    else:
        print('Próximo a jogar:', fila.inicio.nome)

def limpar_fila(fila):
    fila.inicio = None
    fila.fim = None
    print('Fila limpa com sucesso!')

def main():
    fila = Fila()

    while True:
        print('--- SALA DE PARTIDAS ---')
        print('1 - Adicionar jogador')
        print('2 - Simular 1 rodada')
        print('3 - Simular várias rodadas')
        print('4 - Mostrar fila')
        print('5 - Mostrar próximo a jogar')
        print('6 - Limpar fila')
        print('7 - Sair')

        opcao = int(input('Digite uma opção: '))

        if opcao == 1:
            nome = input('Nome do jogador: ')
            adicionar_jogador(fila, nome)
        elif opcao == 2:
            simular_rodada(fila)
        elif opcao == 3:
            n = int(input('Quantas rodadas? '))
            simular_n_rodadas(fila, n)
        elif opcao == 4:
            mostrar_fila(fila)
        elif opcao == 5:
            proximo_jogar(fila)
        elif opcao == 6:
            limpar_fila(fila)
        elif opcao == 7:
            print('Saindo')
            break

main()
