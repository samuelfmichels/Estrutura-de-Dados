class Barracuda:
    def __init__(self, valor):
        self.valor = float(valor)
        self.proximo =  None

    class Lista_encadeada:
        def __init__(self):
            self.inicio = None

    def adicionar(self):
        digitado = float(input('Digite o Número que quer adicionar: '))
        novo = Barracuda(digitado)
        novo.proximo = self.inicio
        self.inicio = novo
        return novo

    def vizualizar(self):
        atual = self.inicio
        while atual is not None:
            print( '- ', atual.valor)
            atual = atual.valor

    def remover(self):
        if self.inicio is None:
            print('Não há itens para serem removidos')
        else:
            digitado = float(input('Digite o Numero que você quer remover?: '))

            if self.inicio.valor == digitado:
                self.inicio = self.inicio.proximo
            elif self.inicio.valor != digitado:
                anterior = atual
                atual = atual.proximo
                while atual is not None:
                    if atual.valor == digitado:
                        anterior.proximo = atual.proximo
                        print('Removido com sucesso!')
                        return
                anterior = atual
                atual = atual.proximo

    lista = Lista_encadeada()

    while True:
        print("\n--- MENU ---")
        print("1. Inserir item")
        print("2. Listar itens")
        print("3. Remover item")
        print("4. Sair")
        
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            lista.adicionar()
        elif opcao == "2":
            lista.vizualizar()
        elif opcao == "3":
            lista.remover()
        elif opcao == "4":
            print("Encerrando...")
            break
        else:
            print("Opção inválida!")

