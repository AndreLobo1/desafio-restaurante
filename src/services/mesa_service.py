from src.models.mesa import Mesa
from src.models.enums import TipoMesa

def cadastrar_mesa(mesas: list, numero: int, tipo: TipoMesa, capacidade_maxima: int):
    """
    Cadastra uma nova mesa no sistema, validando as regras de negócio.
    :param mesas: Lista de mesas existentes no sistema.
    :param numero: Número da mesa a ser cadastrada.
    :param tipo: Tipo da mesa (INDIVIDUAL ou COLETIVA).
    :param capacidade_maxima: Capacidade máxima de pessoas da mesa.
    :return: A nova mesa cadastrada ou None em caso de erro.
    """
    # Verifica se já existe uma mesa com o mesmo número
    if any(mesa.numero == numero for mesa in mesas):  # Itera sobre as mesas para verificar duplicidade
        print(f"Já existe uma mesa com o número {numero}. Não é possível cadastrar novamente.")
        return None

    # Validação para mesas individuais
    if tipo == TipoMesa.INDIVIDUAL and capacidade_maxima > 1:  # Mesas individuais só podem ter capacidade máxima de 1
        print("Mesas individuais só podem ter capacidade máxima de 1 pessoa.")
        return None

    # Cadastra a nova mesa
    nova_mesa = Mesa(numero=numero, tipo=tipo, capacidade_maxima=capacidade_maxima)  # Cria a nova mesa
    mesas.append(nova_mesa)  # Adiciona a mesa à lista de mesas
    print(f"Mesa {numero} cadastrada com sucesso.")  # Confirmação da operação
    return nova_mesa