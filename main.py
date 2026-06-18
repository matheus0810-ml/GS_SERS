# Mission Energy Monitor
# Global Solution 2026.1
# Disciplina: Soluções em Energias Renováveis e Sustentáveis
# Aluno: Matheus Carpinheiro Moreno
# RM: 571770
# Turma: 1CCPX

# Lista que armazena o histórico de todas as leituras da missão
historico_leituras = []


def exibir_menu():
    """
    Função responsável por exibir o menu principal do sistema.
    """
    print("\n====================================================================")
    print("MISSION ENERGY MONITOR")
    print("Monitoramento sustentável de uma missão espacial experimental")
    print("====================================================================")
    print("1. Inserir dados da missão")
    print("2. Visualizar status atual")
    print("3. Executar análise automática")
    print("4. Exibir histórico das leituras")
    print("5. Exibir relatório energético")
    print("6. Encerrar sistema")
    print("====================================================================")


def calcular_indicadores_energeticos(geracao_solar, consumo_modulos):
    """
    Calcula indicadores energéticos considerando que cada leitura
    representa um ciclo de monitoramento com duração de 1 hora.
    """
    duracao_ciclo_horas = 1

    saldo_potencia = geracao_solar - consumo_modulos
    energia_gerada = (geracao_solar * duracao_ciclo_horas) / 1000
    energia_consumida = (consumo_modulos * duracao_ciclo_horas) / 1000

    if consumo_modulos > 0:
        percentual_renovavel = (geracao_solar / consumo_modulos) * 100
        if percentual_renovavel > 100:
            percentual_renovavel = 100
    else:
        percentual_renovavel = 100

    return saldo_potencia, energia_gerada, energia_consumida, percentual_renovavel


def inserir_dados():
    """
    Recebe os dados da missão, calcula os indicadores energéticos,
    executa a análise automática e salva a leitura no histórico.
    """
    print("\n--- Inserir dados da missão ---")

    try:
        temperatura = float(input("Digite a temperatura da nave em °C: "))

        if temperatura < -100 or temperatura > 150:
            print("Erro: temperatura inválida. Digite um valor entre -100 °C e 150 °C.")
            return

        energia = float(input("Digite o nível da bateria em porcentagem: "))

        if energia < 0 or energia > 100:
            print("Erro: o nível da bateria deve estar entre 0% e 100%.")
            return

        comunicacao = int(input("Digite o status da comunicação (1 = ativa, 0 = falha): "))

        if comunicacao != 0 and comunicacao != 1:
            print("Erro: a comunicação deve ser 1 para ativa ou 0 para falha.")
            return

        status_modulo = int(input("Digite o status do módulo operacional (1 = ativo, 0 = falha): "))

        if status_modulo != 0 and status_modulo != 1:
            print("Erro: o status do módulo deve ser 1 para ativo ou 0 para falha.")
            return

        geracao_solar = float(input("Digite a potência gerada pelos painéis solares em watts: "))

        if geracao_solar < 0:
            print("Erro: a geração solar não pode ser negativa.")
            return

        consumo_modulos = float(input("Digite a potência consumida pelos módulos em watts: "))

        if consumo_modulos < 0:
            print("Erro: o consumo dos módulos não pode ser negativo.")
            return

        saldo_potencia, energia_gerada, energia_consumida, percentual_renovavel = (
            calcular_indicadores_energeticos(geracao_solar, consumo_modulos)
        )

        leitura = {
            "temperatura": temperatura,
            "energia": energia,
            "comunicacao": comunicacao,
            "status_modulo": status_modulo,
            "geracao_solar": geracao_solar,
            "consumo_modulos": consumo_modulos,
            "saldo_potencia": saldo_potencia,
            "energia_gerada": energia_gerada,
            "energia_consumida": energia_consumida,
            "percentual_renovavel": percentual_renovavel,
            "status_operacional": "Aguardando análise",
            "alertas": [],
            "decisoes": []
        }

        # A análise é executada automaticamente no momento do cadastro.
        analisar_dados(leitura)
        historico_leituras.append(leitura)

        print("\nDados inseridos e analisados com sucesso!")
        print(f"Status da missão: {leitura['status_operacional']}")

        if len(leitura["alertas"]) == 0:
            print("Nenhum alerta foi identificado.")
        else:
            print("Alertas identificados:")
            for alerta in leitura["alertas"]:
                print(f"- {alerta}")

        if len(leitura["decisoes"]) > 0:
            print("Decisões automáticas:")
            for decisao in leitura["decisoes"]:
                print(f"- {decisao}")

    except ValueError:
        print("Erro: digite apenas valores numéricos.")


def analisar_dados(leitura):
    """
    Analisa temperatura, bateria, comunicação, módulo e equilíbrio energético.
    Também registra decisões automáticas para situações críticas.
    """
    alertas = []
    decisoes = []

    if leitura["temperatura"] > 80:
        alertas.append("Alerta de superaquecimento")
        decisoes.append("Ativar sistema de resfriamento")

    if leitura["temperatura"] < -50:
        alertas.append("Alerta de temperatura extremamente baixa")
        decisoes.append("Ativar sistema de aquecimento e proteção térmica")

    if leitura["energia"] < 20:
        alertas.append("Nível da bateria crítico")
        decisoes.append("Ativar modo de economia de energia")

    if leitura["comunicacao"] == 0:
        alertas.append("Falha de comunicação")
        decisoes.append("Tentar restabelecer o canal de comunicação")

    if leitura["status_modulo"] == 0:
        alertas.append("Falha no módulo operacional")
        decisoes.append("Isolar o módulo e iniciar diagnóstico")

    if leitura["saldo_potencia"] < 0:
        alertas.append("Consumo maior que a geração solar")
        decisoes.append("Reduzir cargas não essenciais para preservar a bateria")

    if leitura["percentual_renovavel"] < 50:
        alertas.append("Baixa participação de energia renovável")
        decisoes.append("Priorizar o uso dos painéis solares e reduzir o consumo")

    if len(alertas) == 0:
        leitura["status_operacional"] = "MISSÃO NORMAL"
    elif len(alertas) <= 2:
        leitura["status_operacional"] = "MISSÃO EM ATENÇÃO"
    else:
        leitura["status_operacional"] = "MISSÃO CRÍTICA"

    leitura["alertas"] = alertas
    leitura["decisoes"] = decisoes

    return alertas, decisoes


def mostrar_leitura(leitura):
    """
    Exibe de forma organizada todos os dados de uma leitura.
    """
    print(f"Temperatura da nave: {leitura['temperatura']:.1f} °C")
    print(f"Nível da bateria: {leitura['energia']:.1f}%")
    print("Comunicação:", "Ativa" if leitura["comunicacao"] == 1 else "Falha")
    print("Módulo operacional:", "Ativo" if leitura["status_modulo"] == 1 else "Falha")
    print(f"Geração solar: {leitura['geracao_solar']:.1f} W")
    print(f"Consumo dos módulos: {leitura['consumo_modulos']:.1f} W")
    print(f"Saldo de potência: {leitura['saldo_potencia']:.1f} W")
    print(f"Energia gerada no ciclo: {leitura['energia_gerada']:.3f} kWh")
    print(f"Energia consumida no ciclo: {leitura['energia_consumida']:.3f} kWh")
    print(f"Participação renovável: {leitura['percentual_renovavel']:.1f}%")
    print(f"Status operacional: {leitura['status_operacional']}")

    if len(leitura["alertas"]) == 0:
        print("Alertas: nenhum")
    else:
        print("Alertas:")
        for alerta in leitura["alertas"]:
            print(f"- {alerta}")

    if len(leitura["decisoes"]) == 0:
        print("Decisões automáticas: nenhuma ação necessária")
    else:
        print("Decisões automáticas:")
        for decisao in leitura["decisoes"]:
            print(f"- {decisao}")


def visualizar_status_atual():
    """
    Mostra a leitura mais recente cadastrada.
    """
    print("\n--- Status atual da missão ---")

    if len(historico_leituras) == 0:
        print("Nenhuma leitura foi cadastrada ainda.")
    else:
        print("Mostrando a leitura mais recente cadastrada:")
        mostrar_leitura(historico_leituras[-1])


def executar_analise_automatica():
    """
    Executa novamente a análise da última leitura cadastrada.
    """
    print("\n--- Análise automática da missão ---")

    if len(historico_leituras) == 0:
        print("Nenhuma leitura foi cadastrada para análise.")
    else:
        ultima_leitura = historico_leituras[-1]

        print("Analisando novamente a leitura mais recente...")
        alertas, decisoes = analisar_dados(ultima_leitura)

        if len(alertas) == 0:
            print("Nenhum alerta encontrado.")
            print("A missão está operando normalmente.")
        else:
            print("Alertas encontrados:")
            for alerta in alertas:
                print(f"- {alerta}")

        if len(decisoes) > 0:
            print("Respostas automáticas:")
            for decisao in decisoes:
                print(f"- {decisao}")

        print(f"Status operacional atualizado: {ultima_leitura['status_operacional']}")


def exibir_historico():
    """
    Exibe todas as leituras armazenadas.
    """
    print("\n--- Histórico das leituras ---")

    if len(historico_leituras) == 0:
        print("Nenhuma leitura foi cadastrada ainda.")
    else:
        contador = 1

        for leitura in historico_leituras:
            print(f"\nLeitura {contador}:")
            print(f"Temperatura: {leitura['temperatura']:.1f} °C")
            print(f"Bateria: {leitura['energia']:.1f}%")
            print("Comunicação:", "Ativa" if leitura["comunicacao"] == 1 else "Falha")
            print("Módulo:", "Ativo" if leitura["status_modulo"] == 1 else "Falha")
            print(f"Geração solar: {leitura['geracao_solar']:.1f} W")
            print(f"Consumo: {leitura['consumo_modulos']:.1f} W")
            print(f"Saldo: {leitura['saldo_potencia']:.1f} W")
            print(f"Uso renovável: {leitura['percentual_renovavel']:.1f}%")
            print(f"Status operacional: {leitura['status_operacional']}")

            contador += 1


def exibir_relatorio_energetico():
    """
    Apresenta um relatório geral com os resultados energéticos
    e sustentáveis de todas as leituras cadastradas.
    """
    print("\n--- Relatório energético e sustentável ---")

    if len(historico_leituras) == 0:
        print("Nenhuma leitura foi cadastrada para gerar o relatório.")
        return

    total_gerado = 0
    total_consumido = 0
    soma_percentual_renovavel = 0
    ciclos_com_saldo_positivo = 0
    ciclos_criticos = 0

    for leitura in historico_leituras:
        total_gerado += leitura["energia_gerada"]
        total_consumido += leitura["energia_consumida"]
        soma_percentual_renovavel += leitura["percentual_renovavel"]

        if leitura["saldo_potencia"] >= 0:
            ciclos_com_saldo_positivo += 1

        if leitura["status_operacional"] == "MISSÃO CRÍTICA":
            ciclos_criticos += 1

    media_renovavel = soma_percentual_renovavel / len(historico_leituras)
    saldo_total_energia = total_gerado - total_consumido

    print(f"Quantidade de ciclos monitorados: {len(historico_leituras)}")
    print(f"Energia solar total gerada: {total_gerado:.3f} kWh")
    print(f"Energia total consumida: {total_consumido:.3f} kWh")
    print(f"Saldo energético total: {saldo_total_energia:.3f} kWh")
    print(f"Participação renovável média: {media_renovavel:.1f}%")
    print(f"Ciclos com saldo de potência positivo: {ciclos_com_saldo_positivo}")
    print(f"Ciclos classificados como críticos: {ciclos_criticos}")

    if saldo_total_energia >= 0 and media_renovavel >= 80:
        print("Avaliação sustentável: desempenho energético eficiente.")
    elif media_renovavel >= 50:
        print("Avaliação sustentável: desempenho moderado, com possibilidade de melhoria.")
    else:
        print("Avaliação sustentável: baixa participação renovável; reduzir o consumo.")


def sistema_principal():
    """
    Função principal do programa.
    Controla o funcionamento do menu interativo.
    """
    while True:
        exibir_menu()

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            inserir_dados()

        elif opcao == "2":
            visualizar_status_atual()

        elif opcao == "3":
            executar_analise_automatica()

        elif opcao == "4":
            exibir_historico()

        elif opcao == "5":
            exibir_relatorio_energetico()

        elif opcao == "6":
            print("\nEncerrando o sistema Mission Energy Monitor...")
            print("Sistema finalizado com sucesso.")
            break

        else:
            print("Opção inválida. Escolha uma opção de 1 a 6.")


# Início do programa
if __name__ == "__main__":
    sistema_principal()
