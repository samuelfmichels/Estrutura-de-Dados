turma =[]
class Aluno: 

    def __init__ (self, nome, nota):

        self.nome = nome
        self.nota = nota
samuel = Aluno('Samuel', [7, 9, 8])
davi = Aluno('Davi', [2, 2.5, 3])
rafael = Aluno('Rafael', [7, 7, 7])

turma.append(samuel)
turma.append(davi)
turma.append(rafael)

for Aluno in turma:
    print('Nome do aluno: ', Aluno.nome)
    media = sum(Aluno.nota) / len(Aluno.nota)
    print('Média do aluno é: ', media)
