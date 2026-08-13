class Produto:
    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

    def mostrar_resumo(self):
        print('Produto, ', self.nome)
        print('Preço, ', self.preco, 'R$')
        print('Quantidade disponível: ', self.quantidade)       

leite = Produto('Leite', 7.99, 50)
leite.mostrar_resumo()

chave = Produto('Chave', 40, 95)
chave.mostrar_resumo()

    
