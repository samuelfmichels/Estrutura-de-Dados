class Barracuda:
    def __init__(self, cliente):
        self.cliente = cliente
        self.proximo = None
        self.anteior = None

def inserir(cliente, inicio_fila, fim_fila):
    novo = Barracuda(cliente)

    if inicio_fila == None:
        fim_fila = novo
        inicio_fila = novo
        return inicio_fila, fim_fila

    fim_fila.proximo = novo
    novo.anteior = fim_fila
    fim_fila = novo
    return inicio_fila, fim_fila

def atender(inicio_fila, fim_fila):
    if inicio_fila == None:
        print('Lista vazia')
        return inicio_fila, fim_fila

    if inicio_fila == fim_fila:
        inicio_fila = None
        fim_fila = None
        return inicio_fila, fim_fila

    inicio_fila = inicio_fila.proximo
    inicio_fila.anterior = None
    return inicio_fila, fim_fila


def percorrer(inicio_fila, fim_fila):
    if inicio_fila == None:
        print('Lista vazia')

    if inicio_fila == fim_fila:
        print('Unico elemento na lista: ', inicio_fila.cliente)
        return inicio_fila, fim_fila

    atual = inicio_fila
    contador = 1

    while atual is not None:
        print(contador, ' - ', atual.cliente)
        atual = atual.proximo
        contador += 1

    print('Lista completamente percorrida')

def mostrar_proximo(inicio_fila, fim_fila):
    if inicio_fila == None:
        print('Lista vazia! ')
        return inicio_fila, fim_fila

    if inicio_fila == fim_fila:
        print('Uníco cliente em espera: ', inicio_fila.cliente)
        return inicio_fila, fim_fila

    print('Proximo paciente: ',inicio_fila.proximo.cliente)
    return inicio_fila, fim_fila

def esta_vazia(inicio_fila, fim_fila):
    if inicio_fila == None:
        print('Lista vazia')
        return inicio_fila, fim_fila
    
    print('Há pessoas na fila! ')
    return inicio_fila, fim_fila

def media_tempo(inicio_fila, fim_fila):
    if inicio_fila == None:
        print('Lista vazia! ')
        return inicio_fila, fim_fila
    if inicio_fila == fim_fila:
        print('Não há tempo de espera pois o cliente está sendo atendido e é o cliente na fila')
        return inicio_fila, fim_fila
    print('Tempo médio de espera: 5 minutos!')
    a = 5
    contador = 1 
    atual = inicio_fila

    print('Usúario sendo atendido: ', inicio_fila.cliente)

    atual = atual.proximo

    print('TEMPO DE ESPERA MÉDIO PARA OS SEGUINTES CLIENTE: ')
    while atual is not None:
        b = contador * a
        print(contador, ' - ', atual.cliente, ' tempo de espera: ', b)
        contador += 1 

        atual = atual.proximo

    print('Lista completamente percorrida')

def main():
    inicio_fila = None
    fim_fila = None
    while True:
        print('1 - adicionar cliente')
        print('2 - atender cliente')
        print('3 - percorrer clientes')
        print('4 - mostrar próximo')
        print('5 - fila está vazia?')
        print('6 - média de tempo')
        print('7 - sair')
        opcao = int(input('Digite a opção desejada: '))

        if opcao == 1:
            novo = input('Digite o nome do paciente: ')
            inicio_fila, fim_fila = inserir(novo,inicio_fila, fim_fila)

        elif opcao == 2:
            inicio_fila, fim_fila = atender(inicio_fila, fim_fila)

        elif opcao == 3:
            percorrer(inicio_fila, fim_fila)

        elif opcao == 4:
            mostrar_proximo(inicio_fila, fim_fila)

        elif opcao == 5:
            esta_vazia(inicio_fila, fim_fila)

        elif opcao == 6:
            media_tempo(inicio_fila, fim_fila)

        elif opcao == 7:
            break

        else:
            print('vai toma no cu padilha')

main()