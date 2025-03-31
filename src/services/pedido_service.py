from src.models.pedido import Pedido

class PedidoService:
    def __init__(self):
        pass

    def criar_pedido(self, mesa):
        """
        Cria um novo pedido associado a uma mesa específica.
        :param mesa: Objeto Mesa onde o pedido será criado.
        :return: O novo pedido criado.
        """
        pedido = Pedido(mesa)  # Cria um novo pedido vinculado à mesa
        print(f"Novo pedido criado para a mesa {mesa.numero}.")  # Confirmação da operação
        return pedido

    def adicionar_prato_ao_pedido(self, pedido, prato, estoque_service):
        """
        Adiciona um prato ao pedido, verificando a disponibilidade dos ingredientes no estoque.
        :param pedido: Objeto Pedido ao qual o prato será adicionado.
        :param prato: Objeto Prato a ser adicionado ao pedido.
        :param estoque_service: Serviço de estoque para verificar disponibilidade de ingredientes.
        """
        if pedido.adicionar_prato(prato, estoque_service):  # Verifica e adiciona o prato ao pedido
            pass
        else:
            print(f"Não foi possível adicionar o prato '{prato.nome}' devido à falta de ingredientes.")