notas = []

class Aluno:
    def __init__(self, nome):
        self.nome = nome
        self.media = 0

    def mostrar_resultado(self):
        print('O nome do aluno é: ', self.nome)

    def calcular_notas(self):
        for i in range(3):
            notas_aplicadas = int(input('Digite a nota do aluno: '))

            while notas_aplicadas < 0 or notas_aplicadas > 10:
                notas_aplicadas = int(input('Digite uma nota válida do aluno: '))

            notas.append(notas_aplicadas)


    def calcular_media(self):
        media = sum(notas) / 3
        self.media = media

    def verificar_aprovacao(self):
        if self.media >= 7:
            print('Aprovado')
            print('Média geral: ', self.media)
            notas.clear()

        else: 
            print('Reprovado')
            print('Media geral: ', self.media)

samuel =  Aluno('Samuel')
samuel.mostrar_resultado()
samuel.calcular_notas()
samuel.calcular_media()
samuel.verificar_aprovacao()


davi =  Aluno('Davi')
davi.mostrar_resultado()
davi.calcular_notas()
davi.calcular_media()
davi.verificar_aprovacao()
