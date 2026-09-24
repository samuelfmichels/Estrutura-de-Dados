class Pilha:
    def __init__(self, dado):
        self.dado = dado
        self.proximo = None


def empilhar(pilha, dado):
    novo = Pilha(dado)

    novo.proximo = pilha
    pilha = novo
    return pilha

def desempilhar(pilha):
    if pilha == None:
        print('Lista vazia! ')
        return pilha

    pilha = pilha.proximo
    return pilha

def topo(pilha):
    if pilha == None:
        print('Lista vazia! ')
        return pilha
    print('O topo é: ', pilha.dado)
    return pilha

def esta_vazia(pilha):
    if pilha == None:
        print('A lista está vazia!')
        return pilha

    else:
        print('Lista tem itens')
        return pilha

def tamanho(pilha):
    if pilha == None:
        print('Lista vazia')
        return pilha
    atual = pilha
    contador = 0
    while atual is not None:
        atual = atual.proximo
        contador +=1

    print('Lista o tamanho de: ', contador, ' itens')
    return pilha

def media(pilha):
    if pilha == None:
        print('Lista vazia! ')
        return pilha

    atual = pilha
    contador = 0
    quantidade = 0

    while atual is not None:
        quantidade += atual.dado
        contador += 1
        atual = atual.proximo

    media = quantidade / contador

    print('A media dos valores é: ', media)

def main():
    pilha = None

    while True:
        print('1 - adicionar pilha')
        print('2 - remover topo pilha') 
        print('3 - mostrar topo')
        print('4 - ver se está vazia')       
        print('5 - tamanho da pilha')
        print('6 - media da pilha')
        print('7 - Sair')

        opcao = int(input('Digite uma opcao: '))

        if opcao == 1:
            novo = int(input('Insira um valor: '))
            pilha = empilhar(pilha, novo)

        elif opcao == 2:
            pilha = desempilhar(pilha)

        elif opcao == 3:
            topo(pilha)

        elif opcao == 4:
            esta_vazia(pilha)

        elif opcao == 5:
            tamanho(pilha)

        elif opcao == 6:
            media(pilha)

        elif opcao == 7:
            print('Saindo... ')
            break

        else:
            print('Vai toma no cu padilha')
main()
