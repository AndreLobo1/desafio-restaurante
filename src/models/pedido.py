class Pedido:
    def __init__(self, mesa):
        # Inicializa um pedido associado a uma mesa
        self.mesa = mesa  # Mesa onde o pedido foi feito
        self.pratos = []  # Lista de pratos do pedido
        self.total = 0.0  # Total do pedido, inicialmente zero

    def adicionar_prato(self, prato, estoque_service):
        """
        Adiciona um prato ao pedido, verificando a disponibilidade de ingredientes no estoque.
        :param prato: Objeto Prato a ser adicionado.
        :param estoque_service: Serviço de estoque para verificar disponibilidade.
        :return: True se o prato foi adicionado, False caso contrário.
        """
        if prato.verificar_ingredientes_disponiveis(estoque_service):  # Verifica se há ingredientes disponíveis
            self.pratos.append(prato)  # Adiciona o prato à lista de pratos
            self.total += prato.preco  # Atualiza o total do pedido
            estoque_service.usar_ingrediente(prato.ingrediente)  # Usa o ingrediente no estoque
            print(f"Prato '{prato.nome}' adicionado ao pedido.")  # Confirma a adição do prato
            return True
        else:
            print(f"Não foi possível adicionar o prato '{prato.nome}' devido à falta de ingredientes.")
            return False

    def calcular_total(self):
        """
        Calcula o total do pedido somando os preços dos pratos.
        :return: Valor total do pedido.
        """
        return sum(prato.preco for prato in self.pratos)  # Soma os preços dos pratos