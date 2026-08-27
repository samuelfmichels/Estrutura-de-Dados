class Musica:
    def __init__(self, id, nome, artista, duracao):
        self.id = id
        self.nome = nome
        self.artista = artista
        self.duracao = duracao
        self.proximo = None
        self.anterior = None

def menu():
    print('\n--- MENU PLAYLIST ---')
    print('1 - Adicionar música')
    print('2 - Listar todas as músicas')
    print('3 - Remover música')
    print('4 - Buscar música')
    print('5 - Mostrar duração total da playlist')
    print('6 - Avançar para a próxima música')
    print('7 - Voltar para a música anterior')
    print('8 - Sair')
    opcao = int(input('Digite uma opção: '))
    return opcao

def menu_busca():
    print('1 - Buscar por Nome')
    print('2 - Buscar por Artista')
    opcao = int(input('Digite a opção de busca: '))
    return opcao

def inserir_musica(lista):
    id = int(input('Digite o ID da música: '))
    nome = input('Digite o nome da música: ')
    artista = input('Digite o artista: ')
    duracao = float(input('Digite a duração (em minutos): '))

    novo = Musica(id, nome, artista, duracao)
    if lista is None:
        lista = novo
        return lista

    novo.proximo = lista
    lista.anterior = novo
    lista = novo
    return lista

def listar(lista, musica_atual):
    if lista is None:
        print('Playlist vazia!')
        return

    aux = lista
    while aux is not None:
        status = ' [TOCANDO AGORA]' if aux == musica_atual else ''
        print('ID:', aux.id, '| Nome:', aux.nome, '| Artista:', aux.artista, '| Duração:', aux.duracao, 'min' + status)
        aux = aux.proximo

def remover(lista, musica_atual):
    if lista is None:
        print('Playlist vazia!')
        return lista, musica_atual

    id_remove = int(input('Digite o ID da música que você deseja remover: '))
    aux = lista

    while aux is not None:
        if aux.id == id_remove:
            if aux == musica_atual:
                musica_atual = aux.proximo if aux.proximo is not None else aux.anterior

            if aux.anterior is None:
                lista = aux.proximo
                if lista is not None:
                    lista.anterior = None
            else:
                aux.anterior.proximo = aux.proximo
                if aux.proximo is not None:
                    aux.proximo.anterior = aux.anterior
            
            print('Música removida com sucesso!')
            return lista, musica_atual
        
        aux = aux.proximo

    print('Música não encontrada!')
    return lista, musica_atual

def buscar(lista):
    if lista is None:
        print('Playlist vazia!')
        return

    opcao_busca = menu_busca()
    aux = lista

    if opcao_busca == 1:
        nome_busca = input('Digite o nome da música: ')
        encontrado = False
        while aux is not None:
            if aux.nome.lower() == nome_busca.lower():
                print('Música encontrada! ID:', aux.id, '| Nome:', aux.nome, '| Artista:', aux.artista, '| Duração:', aux.duracao, 'min')
                encontrado = True
            aux = aux.proximo
        if not encontrado:
            print('Nenhuma música encontrada com esse nome!')

    elif opcao_busca == 2:
        artista_busca = input('Digite o artista: ')
        encontrado = False
        while aux is not None:
            if aux.artista.lower() == artista_busca.lower():
                print('Música encontrada! ID:', aux.id, '| Nome:', aux.nome, '| Artista:', aux.artista, '| Duração:', aux.duracao, 'min')
                encontrado = True
            aux = aux.proximo
        if not encontrado:
            print('Nenhuma música encontrada para esse artista!')

    else:
        print('Opção de busca inválida!')

def mostrar_duracao_total(lista):
    if lista is None:
        print('Playlist vazia! Duração total: 0 min')
        return

    total = 0.0
    aux = lista
    while aux is not None:
        total += aux.duracao
        aux = aux.proximo

    print('Duração total da playlist:', total, 'minutos')

def avancar_musica(musica_atual):
    if musica_atual is None:
        print('Nenhuma música em reprodução!')
        return musica_atual

    if musica_atual.proximo is not None:
        musica_atual = musica_atual.proximo
        print('Avançou para -> ID:', musica_atual.id, '| Nome:', musica_atual.nome, '| Artista:', musica_atual.artista)
    else:
        print('Você já está na última música da playlist!')
    
    return musica_atual

def voltar_musica(musica_atual):
    if musica_atual is None:
        print('Nenhuma música em reprodução!')
        return musica_atual

    if musica_atual.anterior is not None:
        musica_atual = musica_atual.anterior
        print('Voltou para -> ID:', musica_atual.id, '| Nome:', musica_atual.nome, '| Artista:', musica_atual.artista)
    else:
        print('Você já está na primeira música da playlist!')
    
    return musica_atual

playlist = None
musica_atual = None

while True:
    opcao = menu()
    if opcao == 1:
        playlist = inserir_musica(playlist)
        if musica_atual is None:
            musica_atual = playlist
    elif opcao == 2:
        listar(playlist, musica_atual)
    elif opcao == 3:
        playlist, musica_atual = remover(playlist, musica_atual)
    elif opcao == 4:
        buscar(playlist)
    elif opcao == 5:
        mostrar_duracao_total(playlist)
    elif opcao == 6:
        musica_atual = avancar_musica(musica_atual)
    elif opcao == 7:
        musica_atual = voltar_musica(musica_atual)
    elif opcao == 8:
        print('Encerrando player.')
        break
    else:
        print('Opção inválida!')