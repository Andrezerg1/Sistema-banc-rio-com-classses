import contas
import pessoas

class Banco:
    def __init__(
            self,
            agencias: list[int] | None =None,
            contas: list[contas.Conta] | None=None,
            clientes: list[pessoas.Pessoa] | None =None,
        ):
        self.agencias = agencias or []
        self.contas = contas or []
        self.clientes = clientes or []

    def _checa_agencia(self, conta):
        if conta.agencia in self.agencias:
            return True
        else:
            return False
    
    def _checa_conta(self, conta):
        if conta in self.contas:
            return True
        else:
            return False
    
    def _checa_cliente(self, cliente):
        if cliente in self.clientes:
            return True
        else:
            return False

    def _checa_se_a_conta_e_do_cliente(self, cliente, conta):
        if conta is cliente.conta:
            return True
        else:
            return False
    

    def autentica(self, cliente: pessoas.Pessoa, conta: contas.Conta):
        if self._checa_agencia(conta) == False:
            return 'Agência incorreta.'
        elif self._checa_conta(conta) == False:
            return 'Conta incorreta.'
        elif self._checa_cliente(cliente) == False:
            return 'Cliente incorreto'
        elif self._checa_se_a_conta_e_do_cliente(cliente, conta) == False:
            return 'A conta não pertence ao cliente.'
        else:
            return 'Autenticação realizada com sucesso!'

        
    def __repr__(self):
        class_name = type(self).__name__
        attrs = f'({self.agencias!r}, {self.contas!r}, {self.clientes!r})'
        return f'{class_name}{attrs}' 
    
if __name__ == '__main__':
    c1 = pessoas.Cliente('André', 19)
    cc1 = contas.ContaCorrente(100, 222, 0, 0)
    c1.conta = cc1
    c2 = pessoas.Cliente('Maria', 18)
    cp1 = contas.ContaPoupança(100, 223, 100)
    c2.conta = cp1
    banco = Banco()
    banco.clientes.extend([c1, c2])
    banco.contas.extend([cc1, cp1])
    banco.agencias.extend([100, 101])

    if banco.autentica(c1, cc1):
        cc1.depositar(10)
        cc1.detalhes()
        c1.conta.depositar(100)
        print(c1.conta)
