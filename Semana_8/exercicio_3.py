class No:
    def __init__(self, operacao):
        self.operacao = operacao
        self.proximo = None

def inserir(operacao, pilha):
    novo = No(operacao)
    novo.proximo = pilha
    pilha = novo
    return novo

def retirar_ultima( pilha):
    if pilha == None:
        print('Lista vazia, meu cupinxa')
        return pilha

    pilha = pilha.proximo
    return pilha

def resolver_cabeca(pilha):
    if pilha == None:
        print('Lista vazia')
        return pilha

    print('Operação a ser feita: ', pilha.operacao)
    resultado = eval(pilha.operacao)
    print('Resultado da operação é: ', resultado)
    pilha = pilha.proximo
    return pilha

def mostrar_operacoes(pilha):
    if pilha == None:
        print('Lista vazia')
        return pilha
    
    contador = 1
    atual = pilha

    while atual is not None:
        print(contador, ' - ', atual.operacao)
        atual = atual.proximo
        contador += 1

    print('Fim lista')

def main():
    pilha = None
    while True: 
        print('---MENU DOS AFOGADOS--')
        print('1 - inserir operação')
        print('2 - Retirar ultima')
        print('3 - Resolver item mais perto')
        print('4 - Lista Operações faltantes')
        print('5 - Sair')
        opcao = int(input('Digite uma opção: '))    
        if opcao == 1:
            novo = input('Insira a operação: ',)
            pilha = inserir(novo, pilha)
        elif opcao == 2:
            print('Exluido com sucesso! ')
            pilha = retirar_ultima(pilha)
        elif opcao == 3:
            pilha = mostrar_operacoes(pilha)

        elif opcao == 4:
            print('---Listinha dos convocados---')
            pilha = mostrar_operacoes(pilha)
        elif opcao == 5:
            break
        else:
            print('Vai te ferrar meu amiguinho')
            while opcao < 5:
                  opcao = int(input('Digite uma opção válida: '))

main() 
                
