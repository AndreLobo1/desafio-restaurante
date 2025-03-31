class Conta:
    def __init__(self, pedido):
        # Inicializa a conta com base em um pedido
        self.pedido = pedido  # O pedido associado à conta
        self.formaPagamento = None  # Forma de pagamento inicialmente indefinida
        self.valorTotal = 0.0  # Valor total da conta, inicialmente zero

    def emitir_conta(self):
        """
        Emite a conta com o cálculo detalhado dos itens do pedido.
        Exibe os pratos pedidos e o total da conta.
        """
        self.valorTotal = self.pedido.calcular_total()  # Calcula o total do pedido
        print("\n=== DETALHES DA CONTA ===")
        for prato in self.pedido.pratos:
            # Exibe cada prato e seu preço
            print(f"{prato.nome}: R${prato.preco:.2f}")
        print("==========================")
        print(f"Total da conta: R${self.valorTotal:.2f}")  # Exibe o total da conta

    def registrar_pagamento(self, forma_pagamento):
        """
        Registra o pagamento da conta e desativa reservas associadas à mesa.
        :param forma_pagamento: Forma de pagamento escolhida pelo cliente.
        """
        self.formaPagamento = forma_pagamento  # Define a forma de pagamento
        print(f"\nPagamento registrado via {forma_pagamento.value}.")  # Confirma o pagamento
        print(f"Valor pago: R${self.valorTotal:.2f}")  # Exibe o valor pago

        # Verifica se a mesa tem reservas ativas e desativa-as
        mesa = self.pedido.mesa  # Obtém a mesa associada ao pedido
        if hasattr(mesa, 'reservas'):  # Garante que a mesa tem reservas
            for reserva in mesa.reservas:
                if reserva.estaAtiva():  # Verifica se a reserva está ativa
                    reserva.desativar()  # Desativa a reserva