class Estoque:
    def __init__(self):
        # Inicializa o estoque como um dicionário vazio
        self.ingredientes = {}

    def verificar_estoque(self, nome: str) -> bool:
        """
        Verifica se um ingrediente está disponível no estoque.
        :param nome: Nome do ingrediente a ser verificado.
        :return: True se o ingrediente estiver disponível, False caso contrário.
        """
        return nome in self.ingredientes and self.ingredientes[nome] > 0

    def usar_ingrediente(self, nome: str) -> bool:
        """
        Usa uma unidade de um ingrediente no estoque.
        :param nome: Nome do ingrediente a ser usado.
        :return: True se o ingrediente foi usado, False caso contrário.
        """
        if self.verificar_estoque(nome):  # Verifica se o ingrediente está disponível
            self.ingredientes[nome] -= 1  # Decrementa a quantidade do ingrediente
            return True
        return False