class Produto:
    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

    def mostrar_resumo(self):
        print('Produto, ', self.nome)
        print('Preço, ', self.preco, 'R$')
        print('Quantidade disponível: ', self.quantidade)   

    def calculo_total(self):
        calculo = self.preco * self.quantidade
        print('O valor total é: ', calculo)    

leite = Produto('Leite', 7.99, 50)
leite.mostrar_resumo()
leite.calculo_total()

chave = Produto('Chave', 40, 95)
chave.mostrar_resumo()
chave.calculo_total()

    
