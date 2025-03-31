from src.models.enums import TipoMesa
from src.models.reserva import Reserva
from datetime import datetime, timedelta

class Mesa:
    def __init__(self, numero: int, tipo: TipoMesa, capacidade_maxima: int):
        # Inicializa uma mesa com número, tipo e capacidade máxima
        self.numero = numero  # Número da mesa
        self.tipo = tipo  # Tipo da mesa (INDIVIDUAL ou COLETIVA)
        self.capacidadeMaxima = capacidade_maxima  # Capacidade máxima de pessoas
        self.reservas = []  # Lista de reservas associadas à mesa

    def adicionar_reserva(self, data_hora: datetime, numero_pessoas: int):
        """
        Adiciona uma nova reserva à mesa.
        :param data_hora: Data e hora da reserva.
        :param numero_pessoas: Número de pessoas para a reserva.
        """
        reserva = Reserva(data_hora=data_hora, numero_pessoas=numero_pessoas)  # Cria uma nova reserva
        self.reservas.append(reserva)  # Adiciona a reserva à lista de reservas da mesa
        print(f"Reserva adicionada para a mesa {self.numero}:")
        reserva.exibir_detalhes()  # Exibe os detalhes da reserva

    def verificar_disponibilidade(self, data_hora: datetime, numero_pessoas: int) -> bool:
        """
        Verifica se a mesa está disponível para a reserva.
        :param data_hora: Data e hora desejadas para a reserva.
        :param numero_pessoas: Número de pessoas para a reserva.
        :return: True se a mesa estiver disponível, False caso contrário.
        """
        if numero_pessoas > self.capacidadeMaxima:  # Verifica se o número de pessoas excede a capacidade máxima
            return False

        for reserva in self.reservas:  # Itera sobre as reservas existentes
            if (
                reserva.dataHora <= data_hora < reserva.dataHora + timedelta(hours=2)  # Verifica conflitos de horário
                and reserva.numeroPessoas + numero_pessoas > self.capacidadeMaxima  # Verifica capacidade
            ):
                return False

        return True