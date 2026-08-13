class Livro:
    def __init__(self, titulo, autor, numero_paginas):
        self.titulo = titulo
        self.autor = autor
        self.numero_paginas = numero_paginas

    def mostrar_resumo(self):
        print('O titulo é: ', self.titulo)
        print('O autor é: ', self.autor)
        print('Numero de páginas é:', self.numero_paginas)

    def mostrar_la_ele(self):
        if self.numero_paginas <= 100:
            print('Livro Curto')
        else:
            print('Livro longo')

macunaima = Livro('Macunaima', 'Mario de Andrade', 180)
macunaima.mostrar_resumo()
macunaima.mostrar_la_ele()

policarpio = Livro('Histórias Postumas', 'Lima Barreto', 50)
policarpio.mostrar_resumo()
policarpio.mostrar_la_ele()

