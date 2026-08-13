class Produto:
    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

    def mostrar_resumo(self):
        print('Produto, ', self.nome)
        print('Preço, ', self.preco, 'R$')
        print('Quantidade disponível: ', self.quantidade)    

    def atualizacao(self):
        para_soma = int(input('Digite a quantidade adicionada: '))
        print('Quantidade antiga: ', self.quantidade)
        calculo_final = self.quantidade + para_soma
        print('Quantidade atual: ', calculo_final)   

leite = Produto('Leite', 7.99, 50)
leite.mostrar_resumo()
leite.atualizacao()

chave = Produto('Chave', 40, 95)
chave.mostrar_resumo()
chave.atualizacao()


    
