class No:
    def __init__(self, nome, id):
        self.nome = nome
        self.id = id
        self.proximo = None
        self.anterior = None

def menu():
    print('1 - Inserir nó')
    print('2 - Listar nós')
    print('3 - Remover nó')
    print('4 - Verificar se nó existe')
    print('5 - Sair')
    opcao = int(input('Digite uma opção: '))
    return opcao

def menu_busca():
    print('1 - Buscar por Nome')
    print('2 - Buscar por Identificador')
    opcao = int(input('Digite a opção de busca: '))
    return opcao

def inserir_no(lista):
    nome = input('Digite o nome: ')
    id = int(input('Digite o id: '))

    novo = No(nome, id)
    if lista is None:
        lista = novo
        return lista

    novo.proximo = lista
    lista.anterior = novo
    lista = novo
    return lista

def listar(lista):
    if lista is None:
        print('Lista vazia!')
        return

    aux = lista
    while aux is not None:
        print('ID:', aux.id, '| Nome:', aux.nome)
        aux = aux.proximo

def remover(lista):
    if lista is None:
        print('Lista vazia!')
        return lista

    id_remove = int(input('Digite o id do nó que você deseja remover: '))
    aux = lista

    while aux is not None:
        if aux.id == id_remove:
            if aux.anterior is None:
                lista = aux.proximo
                if lista is not None:
                    lista.anterior = None
            else:
                aux.anterior.proximo = aux.proximo
                if aux.proximo is not None:
                    aux.proximo.anterior = aux.anterior
            
            print('Nó removido com sucesso!')
            return lista
        
        aux = aux.proximo

    print('Nó não encontrado!')
    return lista

def verificar_existencia(lista):
    if lista is None:
        print('Lista vazia!')
        return

    opcao_busca = menu_busca()
    aux = lista

    if opcao_busca == 1:
        nome_busca = input('Digite o nome a ser buscado: ')
        while aux is not None:
            if aux.nome.lower() == nome_busca.lower():
                print('Nó encontrado! ID:', aux.id, '| Nome:', aux.nome)
                return
            aux = aux.proximo
        print('Nó com o nome informado não foi encontrado!')

    elif opcao_busca == 2:
        id_busca = int(input('Digite o id a ser buscado: '))
        while aux is not None:
            if aux.id == id_busca:
                print('Nó encontrado! ID:', aux.id, '| Nome:', aux.nome)
                return
            aux = aux.proximo
        print('Nó com o ID informado não foi encontrado!')

    else:
        print('Opção de busca inválida!')

lista_nos = None

while True:
    opcao = menu()
    if opcao == 1:
        lista_nos = inserir_no(lista_nos)
    elif opcao == 2:
        listar(lista_nos)
    elif opcao == 3:
        lista_nos = remover(lista_nos)
    elif opcao == 4:
        verificar_existencia(lista_nos)
    elif opcao == 5:
        print('Encerrando programa.')
        break
    else:
        print('Opção inválida!')