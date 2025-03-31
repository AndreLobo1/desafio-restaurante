from datetime import datetime

class Reserva:
    def __init__(self, data_hora: datetime, numero_pessoas: int):
        # Inicializa uma reserva com data/hora e número de pessoas
        self.dataHora = data_hora  # Data e hora da reserva
        self.numeroPessoas = numero_pessoas  # Número de pessoas
        self.ativa = True  # A reserva começa como ativa

    def estaAtiva(self) -> bool:
        """
        Verifica se a reserva está ativa.
        :return: True se a reserva estiver ativa, False caso contrário.
        """
        return self.ativa

    def desativar(self):
        """
        Desativa a reserva.
        """
        self.ativa = False  # Define a reserva como inativa
        print(f"Reserva para {self.numeroPessoas} pessoas em {self.dataHora.strftime('%Y-%m-%d %H:%M')} foi desativada.")

    def exibir_detalhes(self):
        """
        Exibe os detalhes da reserva, incluindo status (ativa/inativa).
        """
        status = "Ativa" if self.estaAtiva() else "Inativa"
        print(f"Reserva para {self.numeroPessoas} pessoas em {self.dataHora.strftime('%Y-%m-%d %H:%M')} ({status})")