from enum import Enum

class TipoMesa(Enum):
    """
    Define os tipos possíveis de mesa.
    - INDIVIDUAL: Mesa para uma pessoa.
    - COLETIVA: Mesa para múltiplas pessoas.
    """
    INDIVIDUAL = "INDIVIDUAL"
    COLETIVA = "COLETIVA"

class TipoPrato(Enum):
    """
    Define os tipos possíveis de prato.
    - ENTRADA: Prato de entrada.
    - PRINCIPAL: Prato principal.
    - SOBREMESA: Sobremesa.
    """
    ENTRADA = "ENTRADA"
    PRINCIPAL = "PRINCIPAL"
    SOBREMESA = "SOBREMESA"

class StatusPedido(Enum):
    """
    Define os status possíveis de um pedido.
    - ABERTO: Pedido ainda não finalizado.
    - FECHADO: Pedido finalizado.
    """
    ABERTO = "ABERTO"
    FECHADO = "FECHADO"

class FormaPagamento(Enum):
    """
    Define as formas de pagamento disponíveis.
    - DINHEIRO: Pagamento em dinheiro.
    - CARTAO: Pagamento com cartão.
    - PIX: Pagamento via PIX.
    - VR: Pagamento com vale-refeição.
    """
    DINHEIRO = "DINHEIRO"
    CARTAO = "CARTAO"
    PIX = "PIX"
    VR = "VR"