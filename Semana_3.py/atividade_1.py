class Produto:

    def __init__(self, nome, preco, quantidade_estoque):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade_estoque

    def mostrar_info(self):
        print('Produto: ', self.nome )
        print('Preço: ', self.preco)
        print('Quantidade disponível para compra: ', self.quantidade)

    def adicionar_produto(self):
        while True:
            print('Você deseja adicionar estoque a ', self.nome, '?')
            print('1 - Sim')
            print('2 - Não')
            opcao = int(input('Digite uma opção: '))
            
            if opcao == 1:
                quantidade = int(input('Digite a quantidade: '))
                self.quantidade += quantidade

            if opcao == 2:
                break

    def venda(self):
        while True:
            print('Você deseja vender ', self.nome, '?')
            print('1 - Sim')
            print('2 - Não')
            opcao = int(input('Digite uma opção: '))
            
            if opcao == 1:
                quantidade = int(input('Digite a quantidade: '))
                if quantidade > self.quantidade:
                    print('impossível realizar venda')
                else:
                    print('Venda realizada com sucesso, foram comprados um total de ', quantidade, 'itens')
                    self.quantidade -= quantidade

            if opcao == 2:
                break

    def preco_total(self):
        mult = self.quantidade * self.preco
        print('O valor total disponível de ', self.nome, 'é: R$', mult)


morango = Produto('Morango', 5, 100)
morango.mostrar_info()
morango.adicionar_produto()
morango.venda()
morango.preco_total()

banana = Produto('Banana', 10, 90)
banana.mostrar_info()
banana.adicionar_produto()
banana.venda()
banana.preco_total()

maca = Produto('Maça', 15, 60)
maca.mostrar_info()
maca.adicionar_produto()
maca.venda()
maca.preco_total()

