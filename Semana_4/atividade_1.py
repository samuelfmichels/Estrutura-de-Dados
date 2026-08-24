class Barracuda:
    def __init__(self, nome, id, nota):
        self.nome = nome
        self.id = id
        self.nota = nota
        self.proximo = None
        self.anterior = None

def menu():
    print('1 - Inserir aluno')
    print('2 - Listar aluno')
    print('3 - Remover aluno')
    print('4 - Mostrar situação aluno')
    print('5 - Listar alunos classificados')
    print('6 - Sair')
    opcao = int(input('Digite uma opção: '))
    return opcao

def inserir_aluno(lista):
    nome = input('Digite o nome do aluno: ')
    id = int(input('Digite o id do aluno: '))
    nota = float(input('Digite a nota do aluno: '))

    novo = Barracuda(nome, id, nota)
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
        print('ID:', aux.id, 'Nome:', aux.nome, 'Nota:', aux.nota)
        aux = aux.proximo

def remover(lista):
    if lista is None:
        print('Lista vazia!')
        return lista

    id_remove = int(input('Digite o id do aluno que você deseja remover: '))
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
            
            print('Aluno removido com sucesso!')
            return lista
        
        aux = aux.proximo

    print('Aluno não encontrado!')
    return lista

def mostrar_situacao(lista):
    if lista is None:
        print('Lista vazia!')
        return

    aux = lista
    while aux is not None:
        if aux.nota >= 7.0:
            situacao = 'Aprovado'
        elif aux.nota >= 4.0:
            situacao = 'Exame'
        else:
            situacao = 'Reprovado'
        
        print('ID:', aux.id, 'Nome:', aux.nome, 'Nota:', aux.nota, 'Situação:', situacao)
        aux = aux.proximo

def listar_classificados(lista):
    if lista is None:
        print('Lista vazia!')
        return

    print('--- APROVADOS (Nota >= 7.0) ---')
    aux = lista
    while aux is not None:
        if aux.nota >= 7.0:
            print('ID:', aux.id, 'Nome:', aux.nome, 'Nota:', aux.nota)
        aux = aux.proximo

    print('--- EXAME (Nota entre 4.0 e 6.9) ---')
    aux = lista
    while aux is not None:
        if 4.0 <= aux.nota < 7.0:
            print('ID:', aux.id, 'Nome:', aux.nome, 'Nota:', aux.nota)
        aux = aux.proximo

    print('--- REPROVADOS (Nota < 4.0) ---')
    aux = lista
    while aux is not None:
        if aux.nota < 4.0:
            print('ID:', aux.id, 'Nome:', aux.nome, 'Nota:', aux.nota)
        aux = aux.proximo

lista_alunos = None

while True:
    opcao = menu()
    if opcao == 1:
        lista_alunos = inserir_aluno(lista_alunos)
    elif opcao == 2:
        listar(lista_alunos)
    elif opcao == 3:
        lista_alunos = remover(lista_alunos)
    elif opcao == 4:
        mostrar_situacao(lista_alunos)
    elif opcao == 5:
        listar_classificados(lista_alunos)
    elif opcao == 6:
        print('Encerrando programa.')
        break
    else:
        print('Opção inválida!')


                
                
