agenda = []

class Contato:
    def __init__(self, nome, contato, email):
        self.nome = nome
        self.contato = contato
        self.email = email

fernando = Contato('Fernando ', 51996525124, 'fernandinhobeiramar@gmail.com')
marcos = Contato('Marcos', 51663245781, 'Marcola@gmail.com')
fiori = Contato('Fiori', 5142489635, 'Fiorilegalidade@gmail.com')

agenda.append(fernando)
agenda.append(marcos)
agenda.append(fiori)

for i in range (len(agenda)):
    print(agenda[i].nome)
    print(agenda[i].contato)
