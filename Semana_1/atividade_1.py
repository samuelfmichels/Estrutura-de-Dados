class Aluno:
    def __init__(self, nome, frequencia, media_geral):
        self.nome= nome
        self.frequencia = frequencia
        self.media = media_geral

    def mostrar_situacao(self):
        print('Nome: ', self.nome)
        print('Frequencia: ', self.frequencia, '%')
        print('Media: ', self.media)

joao = Aluno('João', 76, 7.8)
joao.mostrar_situacao()

maria = Aluno('Maria', 80, 8.5)
maria.mostrar_situacao()
