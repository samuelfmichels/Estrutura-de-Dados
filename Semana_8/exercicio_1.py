class No:
    def __init__(self, nome):
        self.nome = nome
        self.proximo = None
        self.anterior = None

def inserir(nome, inicio_fila, fim_fila):
    novo = No(nome)

    if inicio_fila is None:
        print('Lista vazia, adicionando elemento')
        inicio_fila = novo
        fim_fila = novo
        return fim_fila, inicio_fila

    fim_fila.proximo = novo
    novo.anterior = fim_fila
    fim_fila = novo
    return inicio_fila, fim_fila

def atendimento(inicio_fila, fim_fila):
    if inicio_fila == None:
        print('Lista vazia')
        return inicio_fila, fim_fila

    if inicio_fila == fim_fila:
        print('Unico elemento na lista')
        print('Atendendo paciente: ', inicio_fila.nome)
        inicio_fila = fim_fila = None
        return inicio_fila, fim_fila

    print('Atendendo paciente: ', inicio_fila.nome)
    inicio_fila = inicio_fila.proximo
    inicio_fila.anterior = None

    print('Proximo da fila é: ', inicio_fila.nome)

    contador = 0
    atual = inicio_fila
    while atual is not None:
        atual = atual.proximo
        contador += 1

    print('Ainda restam ',contador, 'pessoas')

    return inicio_fila, fim_fila

def main():
    inicio_fila = None
    fim_fila = None
    while True:
        print('1 - Adicionar Paciente ')
        print('2 - Atender Paciente ')
        print('3 - Sair')
        opcao = int(input('Digite uma opção: '))
        if opcao == 1: 
            novo = input('Digite o nome do paciente: ')
            inicio_fila , fim_fila = inserir(novo, inicio_fila, fim_fila)

        elif opcao == 2: 
           inicio_fila, fim_fila = atendimento(inicio_fila, fim_fila)

        elif opcao == 3:
            break

        else:
             while opcao <= 4:
                  opcao = int(input('Digite uma opção: '))

main()

                 
