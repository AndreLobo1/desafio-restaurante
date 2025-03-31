from src.models.conta import Conta

class ContaService:
    @staticmethod
    def emitir_conta(conta):
        """
        Emite a conta para um pedido específico.
        Chama o método 'emitir_conta' da classe Conta, que exibe os detalhes da conta, incluindo os pratos e o total.
        :param conta: Objeto Conta contendo os dados do pedido.
        """
        conta.emitir_conta()

    @staticmethod
    def registrar_pagamento(conta, forma_pagamento):
        """
        Registra o pagamento de uma conta.
        Chama o método 'registrar_pagamento' da classe Conta, que processa o pagamento e desativa reservas associadas à mesa.
        :param conta: Objeto Conta contendo os dados do pedido.
        :param forma_pagamento: Forma de pagamento escolhida pelo cliente.
        """
        conta.registrar_pagamento(forma_pagamento)