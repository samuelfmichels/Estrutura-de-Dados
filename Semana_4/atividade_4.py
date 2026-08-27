class Tarefa:
    def __init__(self, descricao, prazo):
        self.descricao = descricao
        self.prazo = prazo
        self.proximo = None
        self.anterior = None

def menu():
    print('\n--- AGENDA DE TAREFAS ---')
    print('1 - Inserir nova tarefa')
    print('2 - Remover tarefa existente')
    print('3 - Listar todas as tarefas')
    print('4 - Sair do programa')
    opcao = int(input('Digite uma opção: '))
    return opcao

def inserir_tarefa(lista):
    descricao = input('Digite a descrição da tarefa: ')
    prazo = input('Digite o prazo da tarefa (ex: 2025-08-10): ')

    novo = Tarefa(descricao, prazo)
    if lista is None:
        lista = novo
        return lista

    novo.proximo = lista
    lista.anterior = novo
    lista = novo
    return lista

def remover_tarefa(lista):
    if lista is None:
        print('Lista vazia!')
        return lista

    desc_remove = input('Digite a descrição da tarefa que você deseja remover: ')
    aux = lista

    while aux is not None:
        if aux.descricao.lower() == desc_remove.lower():
            if aux.anterior is None:
                lista = aux.proximo
                if lista is not None:
                    lista.anterior = None
            else:
                aux.anterior.proximo = aux.proximo
                if aux.proximo is not None:
                    aux.proximo.anterior = aux.anterior
            
            print('Tarefa removida com sucesso!')
            return lista
        
        aux = aux.proximo

    print('Tarefa não encontrada!')
    return lista

def listar_tarefas(lista):
    if lista is None:
        print('Lista vazia!')
        return

    aux = lista
    while aux.proximo is not None:
        aux = aux.proximo

    print('\n--- TAREFAS NA ORDEM DE CADASTRO ---')
    while aux is not None:
        print('Descrição:', aux.descricao, '| Prazo:', aux.prazo)
        aux = aux.anterior

lista_tarefas = None

while True:
    opcao = menu()
    if opcao == 1:
        lista_tarefas = inserir_tarefa(lista_tarefas)
    elif opcao == 2:
        lista_tarefas = remover_tarefa(lista_tarefas)
    elif opcao == 3:
        listar_tarefas(lista_tarefas)
    elif opcao == 4:
        print('Encerrando programa.')
        break
    else:
        print('Opção inválida!')