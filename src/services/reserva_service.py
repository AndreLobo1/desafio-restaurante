from datetime import datetime, timedelta
from src.models.mesa import Mesa

def verificar_disponibilidade_mesa(mesa: Mesa, data_hora: datetime, numero_pessoas: int) -> bool:
    """
    Verifica se uma mesa específica está disponível para o horário e capacidade especificados.
    :param mesa: Objeto Mesa a ser verificada.
    :param data_hora: Data e hora desejadas para a reserva.
    :param numero_pessoas: Número de pessoas para a reserva.
    :return: True se a mesa estiver disponível, False caso contrário.
    """
    # Verifica se o número de pessoas excede a capacidade máxima da mesa
    if numero_pessoas > mesa.capacidadeMaxima:
        return False

    # Verifica conflitos de reservas existentes
    for reserva in mesa.reservas:  # Itera sobre as reservas da mesa
        if (
            reserva.dataHora <= data_hora < reserva.dataHora + timedelta(hours=2)  # Verifica intervalo de 2 horas
            and reserva.numeroPessoas + numero_pessoas > mesa.capacidadeMaxima  # Verifica capacidade
        ):
            return False

    return True


def encontrar_primeira_mesa_disponivel(mesas: list, data_hora: datetime, numero_pessoas: int):
    """
    Encontra a primeira mesa disponível para o horário e capacidade especificados.
    :param mesas: Lista de objetos Mesa disponíveis no sistema.
    :param data_hora: Data e hora desejadas para a reserva.
    :param numero_pessoas: Número de pessoas para a reserva.
    :return: A primeira mesa disponível ou None se nenhuma estiver disponível.
    """
    for mesa in mesas:  # Itera sobre todas as mesas
        if verificar_disponibilidade_mesa(mesa, data_hora, numero_pessoas):  # Verifica disponibilidade da mesa
            return mesa  # Retorna a primeira mesa disponível
    return None  # Retorna None se nenhuma mesa estiver disponível