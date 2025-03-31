from src.models.enums import TipoPrato

class Prato:
    def __init__(self, nome: str, tipo: TipoPrato, preco: float, ingrediente: str):
        # Inicializa um prato com nome, tipo, preço e ingrediente principal
        self.nome = nome  # Nome do prato
        self.tipo = tipo  # Tipo do prato (ENTRADA, PRINCIPAL, SOBREMESA)
        self.preco = preco  # Preço do prato
        self.ingrediente = ingrediente  # Ingrediente principal

    def exibir_detalhes(self):
        """
        Exibe os detalhes do prato, incluindo nome, tipo e preço.
        """
        print(f"Prato: {self.nome}, Tipo: {self.tipo.value}, Preço: R${self.preco:.2f}")

    def verificar_ingredientes_disponiveis(self, estoque_service) -> bool:
        """
        Verifica se o ingrediente principal do prato está disponível no estoque.
        :param estoque_service: Serviço de estoque para verificar disponibilidade.
        :return: True se o ingrediente estiver disponível, False caso contrário.
        """
        return estoque_service.verificar_disponibilidade(self.ingrediente)


# Lista de pratos pré-definidos
PRATOS_PREDEFINIDOS = [
    Prato(nome="Salada", tipo=TipoPrato.ENTRADA, preco=15.0, ingrediente="ALFACE"),
    Prato(nome="Frango Frito", tipo=TipoPrato.PRINCIPAL, preco=40.0, ingrediente="FRANGO"),
    Prato(nome="Fritas", tipo=TipoPrato.PRINCIPAL, preco=25.0, ingrediente="BATATA"),
    Prato(nome="Hamburguer", tipo=TipoPrato.PRINCIPAL, preco=35.0, ingrediente="CARNE"),
    Prato(nome="Pudim", tipo=TipoPrato.SOBREMESA, preco=10.0, ingrediente="LEITE"),
]