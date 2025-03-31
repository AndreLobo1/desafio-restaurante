from src.models.estoque import Estoque

class EstoqueService:
    def __init__(self):
        # Inicializa o serviço de estoque com uma instância da classe Estoque
        self.estoque = Estoque()

    def adicionar_ingrediente(self, nome: str, quantidade: int):
        """
        Adiciona um ingrediente ao estoque ou incrementa sua quantidade se já existir.
        :param nome: Nome do ingrediente a ser adicionado.
        :param quantidade: Quantidade a ser adicionada ao estoque.
        """
        if nome in self.estoque.ingredientes:  # Verifica se o ingrediente já existe no estoque
            self.estoque.ingredientes[nome] += quantidade  # Incrementa a quantidade existente
        else:
            self.estoque.ingredientes[nome] = quantidade  # Adiciona o ingrediente ao estoque
        print(f"{quantidade} unidades de '{nome}' adicionadas ao estoque.")  # Confirmação da operação

    def verificar_disponibilidade(self, nome: str) -> bool:
        """
        Verifica se um ingrediente está disponível no estoque.
        :param nome: Nome do ingrediente a ser verificado.
        :return: True se o ingrediente estiver disponível, False caso contrário.
        """
        if self.estoque.verificar_estoque(nome):  # Usa o método da classe Estoque para verificar disponibilidade
            print(f"Ingrediente '{nome}' disponível no estoque.")
            return True
        else:
            print(f"Ingrediente '{nome}' indisponível no estoque.")
            return False

    def usar_ingrediente(self, nome: str) -> bool:
        """
        Usa uma unidade de um ingrediente no estoque.
        :param nome: Nome do ingrediente a ser usado.
        :return: True se o ingrediente foi usado, False caso contrário.
        """
        if self.estoque.usar_ingrediente(nome):  # Usa o método da classe Estoque para decrementar o ingrediente
            print(f"1 unidade de '{nome}' usada do estoque.")
            return True
        else:
            print(f"Não há '{nome}' suficiente no estoque.")
            return False