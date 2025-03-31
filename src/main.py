from datetime import datetime
from src.models.mesa import Mesa
from src.models.enums import TipoMesa, FormaPagamento
from src.models.conta import Conta
from src.models.prato import PRATOS_PREDEFINIDOS
from src.services.mesa_service import cadastrar_mesa
from src.services.pedido_service import PedidoService
from src.services.estoque_service import EstoqueService
from src.services.conta_service import ContaService
from src.services.reserva_service import encontrar_primeira_mesa_disponivel

def menu_interativo():
    # Dados iniciais do restaurante
    mesas = [
        Mesa(numero=1, tipo=TipoMesa.COLETIVA, capacidade_maxima=4),
        Mesa(numero=2, tipo=TipoMesa.COLETIVA, capacidade_maxima=2),
        Mesa(numero=3, tipo=TipoMesa.COLETIVA, capacidade_maxima=6),
        Mesa(numero=4, tipo=TipoMesa.COLETIVA, capacidade_maxima=8),
    ]

    # Reservas pré-existentes
    mesas[1].adicionar_reserva(data_hora=datetime(2024, 10, 28, 20, 30), numero_pessoas=2)
    mesas[0].adicionar_reserva(data_hora=datetime(2024, 10, 28, 19, 0), numero_pessoas=4)

    # Serviços
    estoque_service = EstoqueService()  # Inicializa o serviço de estoque
    estoque_service.adicionar_ingrediente("ALFACE", 10)  # Adiciona ingredientes ao estoque
    estoque_service.adicionar_ingrediente("FRANGO", 5)
    estoque_service.adicionar_ingrediente("BATATA", 20)
    estoque_service.adicionar_ingrediente("CARNE", 15)
    estoque_service.adicionar_ingrediente("LEITE", 8)

    pedido_service = PedidoService()  # Inicializa o serviço de pedidos
    conta_service = ContaService()  # Inicializa o serviço de contas

    # Pedidos ativos
    pedidos_ativos = {}  # Dicionário para rastrear pedidos ativos por mesa

    while True:
        print("\n=== MENU ===")
        print("1. Cadastrar mesa")
        print("2. Registrar pedido")
        print("3. Emitir conta")
        print("4. Listar mesas cadastradas")
        print("5. Fazer reserva")
        print("6. Visualizar reservas por mesa")
        print("7. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            # Cadastrar nova mesa
            numero = int(input("Número da mesa: "))
            
            # Menu para escolher o tipo da mesa
            print("Escolha o tipo da mesa:")
            print("1. Coletiva")
            print("2. Individual")
            tipo_escolha = input("Digite o número correspondente ao tipo da mesa: ")
            tipo = TipoMesa.COLETIVA if tipo_escolha == "1" else TipoMesa.INDIVIDUAL

            capacidade_maxima = int(input("Capacidade máxima: "))
            cadastrar_mesa(mesas, numero, tipo, capacidade_maxima)  # Chama o serviço para cadastrar a mesa

        elif opcao == "2":
            # Registrar novo pedido
            numero_mesa = int(input("Número da mesa para o pedido: "))
            mesa = next((m for m in mesas if m.numero == numero_mesa), None)  # Busca a mesa pelo número
            if not mesa:
                print("Mesa não encontrada.")
                continue

            if mesa.numero not in pedidos_ativos:  # Verifica se já existe um pedido ativo para a mesa
                pedido = pedido_service.criar_pedido(mesa)  # Cria um novo pedido
                pedidos_ativos[mesa.numero] = pedido  # Registra o pedido como ativo
            else:
                pedido = pedidos_ativos[mesa.numero]  # Usa o pedido existente

            print("Pratos disponíveis:")  # Exibe os pratos pré-definidos
            for i, prato in enumerate(PRATOS_PREDEFINIDOS, start=1):
                print(f"{i}. {prato.nome} ({prato.tipo.value}) - R${prato.preco:.2f}")

            escolha_prato = int(input("Escolha o número do prato: ")) - 1  # Solicita a escolha do prato
            if 0 <= escolha_prato < len(PRATOS_PREDEFINIDOS):  # Valida a escolha do prato
                prato = PRATOS_PREDEFINIDOS[escolha_prato]
                pedido_service.adicionar_prato_ao_pedido(pedido, prato, estoque_service)  # Adiciona o prato ao pedido
            else:
                print("Opção inválida.")

        elif opcao == "3":
            # Emitir conta
            numero_mesa = int(input("Número da mesa para emitir a conta: "))
            mesa = next((m for m in mesas if m.numero == numero_mesa), None)  # Busca a mesa pelo número
            if not mesa or mesa.numero not in pedidos_ativos:  # Verifica se há um pedido ativo para a mesa
                print("Nenhum pedido ativo para esta mesa.")
                continue

            pedido = pedidos_ativos[mesa.numero]  # Obtém o pedido ativo
            conta = Conta(pedido)  # Cria uma conta com base no pedido
            conta_service.emitir_conta(conta)  # Emite a conta

            forma_pagamento_str = input("Forma de pagamento (DINHEIRO/CARTAO/PIX/VR): ").upper()
            forma_pagamento = FormaPagamento[forma_pagamento_str]  # Converte a entrada para o enum FormaPagamento
            conta_service.registrar_pagamento(conta, forma_pagamento)  # Registra o pagamento

            pago = input("A conta foi paga? (S/N): ").upper()
            if pago == "S":  # Verifica se o pagamento foi confirmado
                print("Conta paga com sucesso!")
                del pedidos_ativos[mesa.numero]  # Remove o pedido após o pagamento
            else:
                print("Conta pendente.")

        elif opcao == "4":
            # Listar mesas cadastradas
            print("\nMesas cadastradas:")
            for mesa in mesas:  # Itera sobre as mesas e exibe seus detalhes
                print(f"Mesa {mesa.numero} - Tipo: {mesa.tipo.value}, Capacidade: {mesa.capacidadeMaxima}")

        elif opcao == "5":
            # Fazer reserva
            data_str = input("Data (AAAA-MM-DD): ")
            hora_str = input("Hora (HH:MM): ")
            numero_pessoas = int(input("Número de pessoas: "))

            try:
                data_hora = datetime.strptime(f"{data_str} {hora_str}", "%Y-%m-%d %H:%M")  # Converte a entrada para datetime
            except ValueError:
                print("Formato de data ou hora inválido. Use AAAA-MM-DD HH:MM.")
                continue

            mesa_disponivel = encontrar_primeira_mesa_disponivel(mesas, data_hora, numero_pessoas)  # Encontra uma mesa disponível
            if mesa_disponivel:
                mesa_disponivel.adicionar_reserva(data_hora, numero_pessoas)  # Adiciona a reserva à mesa
                print(f"Reserva realizada com sucesso na mesa {mesa_disponivel.numero}.")
            else:
                print("Não há mesas disponíveis para a data, hora e número de pessoas informados.")

        elif opcao == "6":
            # Visualizar reservas por mesa
            numero_mesa = int(input("Número da mesa: "))
            mesa = next((m for m in mesas if m.numero == numero_mesa), None)  # Busca a mesa pelo número
            if not mesa:
                print("Mesa não encontrada.")
                continue

            if not mesa.reservas:  # Verifica se há reservas para a mesa
                print(f"Nenhuma reserva encontrada para a mesa {numero_mesa}.")
            else:
                print(f"Reservas para a mesa {numero_mesa}:")
                for reserva in mesa.reservas:  # Exibe os detalhes de cada reserva
                    reserva.exibir_detalhes()

        elif opcao == "7":
            # Sair do sistema
            print("Encerrando o sistema...")
            break

        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    menu_interativo()  # Inicia o menu interativo