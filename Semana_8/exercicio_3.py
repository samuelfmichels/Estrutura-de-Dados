pilha = [
    'Carro 1', 'Carro 2', 'Carro 3', 'Carro 4', 'Carro 5',
    'Carro 6', 'Carro 7', 'Carro 8', 'Carro 9', 'Carro 10',
    'Carro 11', 'Carro 12', 'Carro 13', 'Carro 14', 'Carro 15',
    'Carro 16', 'Carro 17', 'Carro 18', 'Carro 19', 'Carro 20'
]

def achar_alvo(pilha, alvo):
    if not pilha:
        print('Lista vazia, meu amiguinho')
        return pilha

    achou = False
    while len(pilha) > 0:
        topo = pilha[-1]

        if topo == alvo:
            print('Carro tirado com sucesso:', pilha.pop())
            achou = True
            break

        print('Saindo para dar passagem:', pilha.pop())

    if not achou:
        print('Impossível localizar!')

    return pilha

def mostrar_garagem(pilha):
    if not pilha:
        print('Garagem vazia!')
        return

    print('\n--- CARROS NA GARAGEM ---')
    contador = 1
    for carro in reversed(pilha):
        print(contador, '-', carro)
        contador += 1

def main():
    while True:
        print('\n--- GARAGEM DOS AFOGADOS ---')
        print('1 - Ver carros na garagem')
        print('2 - Retirar carro especifico')
        print('3 - Sair')
        
        opcao = int(input('Digite uma opção: '))

        if opcao == 1:
            mostrar_garagem(pilha)
        elif opcao == 2:
            alvo = input('Digite o nome do carro (ex: Carro 15): ')
            achar_alvo(pilha, alvo)
        elif opcao == 3:
            print('Saindo...')
            break

main()
