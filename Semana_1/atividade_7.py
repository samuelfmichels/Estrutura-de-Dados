class Funcionario:
    def __init__(self, nome, salario, cargo):
        self.nome = nome
        self.salario = salario
        self.cargo = cargo

    def mostrar_resultado(self):
        print('Nome do colaborador: ', self.nome)
        print('Cargo do Colaborador: ', self.cargo)

    def calcular_bonus(self):
        print('Salário do colaborador antes do reajuste: ', self.salario)

        if self.cargo == 'gerente':
            bonus_siliconado = self.salario * 1.10
            print('O novo salário reajustado do colaborador é: ', bonus_siliconado)

        else:
            bonus_siliconado = self.salario * 1.05
            print('O novo salário reajustado do colaborador é: ', bonus_siliconado)


maria = Funcionario('Maria', 1700, 'peão')
maria.mostrar_resultado()
maria.calcular_bonus()

joão = Funcionario('João', 2000, 'gerente')
joão.mostrar_resultado()
joão.calcular_bonus()
