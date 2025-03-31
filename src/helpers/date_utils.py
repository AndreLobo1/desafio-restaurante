from datetime import datetime, timedelta

def is_within_range(date: datetime, start: datetime, end: datetime) -> bool:
    """
    Verifica se uma data está dentro de um intervalo específico.
    :param date: Data a ser verificada.
    :param start: Início do intervalo.
    :param end: Fim do intervalo.
    :return: True se a data estiver dentro do intervalo, False caso contrário.
    """
    return start <= date <= end

def format_datetime(date: datetime) -> str:
    """
    Formata uma data/hora para exibição no formato DD/MM/YYYY HH:MM.
    :param date: Data/hora a ser formatada.
    :return: Data/hora formatada como string.
    """
    return date.strftime("%d/%m/%Y %H:%M")

def add_hours(date: datetime, hours: int) -> datetime:
    """
    Adiciona horas a uma data/hora.
    :param date: Data/hora original.
    :param hours: Número de horas a serem adicionadas.
    :return: Nova data/hora após adicionar as horas.
    """
    return date + timedelta(hours=hours)