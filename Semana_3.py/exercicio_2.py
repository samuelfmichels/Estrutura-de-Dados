class ContaBancaria:
    def __init__(self, titular, numero_conta, saldo):
        self.titular = titular
        self.numero_conta = numero_conta
        self.saldo = saldo

    def consultar_saldo(self):
        print('Conta:', self.numero_conta, '| Titular:', self.titular, '| Saldo:', self.saldo)

    def depositar(self, valor):
        if valor <= 0:
            print('Valor de depósito inválido!')
            return
        
        self.saldo = self.saldo + valor
        print('Depósito realizado com sucesso!')
        self.consultar_saldo()

    def sacar(self, valor):
        if valor <= 0:
            print('Valor de saque inválido!')
            return
        
        if valor > self.saldo:
            print('Saldo insuficiente!')
            return
        
        self.saldo = self.saldo - valor
        print('Saque realizado com sucesso!')
        self.consultar_saldo()

    def transferir(self, conta_destino, valor):
        if valor <= 0:
            print('Valor de transferência inválido!')
            return
        
        if valor > self.saldo:
            print('Saldo insuficiente para transferir!')
            return
        
        self.saldo = self.saldo - valor
        conta_destino.saldo = conta_destino.saldo + valor
        print('Transferência realizada com sucesso!')
        print('Saldo da conta de origem:')
        self.consultar_saldo()
        print('Saldo da conta de destino:')
        conta_destino.consultar_saldo()

conta1 = ContaBancaria('Carlos Silva', 101, 500.0)
conta2 = ContaBancaria('Mariana Souza', 202, 200.0)

conta1.consultar_saldo()
conta2.consultar_saldo()

conta1.depositar(150.0)
conta2.sacar(300.0)
conta2.sacar(50.0)
conta1.transferir(conta2, 200.0)
conta1.depositar(-50.0)

conta1.consultar_saldo()
conta2.consultar_saldo()