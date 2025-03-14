acoes_2024 = [
    {'preco': [100, 105, 110, 108, 109, 112, 115, 118, 120, 122, 124, 125], 'dividendo': 5},  # Ação 1
    {'preco': [50, 52, 55, 53, 54, 56, 58, 59, 60, 62, 63, 65], 'dividendo': 3},           # Ação 2
    {'preco': [200, 205, 210, 208, 210, 212, 215, 218, 220, 225, 230, 235], 'dividendo': 10} # Ação 3
]

# Função recursiva para simular o investimento e calcular os marcos
def investimento(investido, meses, acoes, valor_investido_total, dividendos_recebidos, juros_compostos):
    # Verifica os marcos
    if valor_investido_total >= 1000000:
        print(f'Marca de R$ 1.000.000,00 atingida em {meses//12} anos e {meses%12} meses')
        print(f'Valor investido até o marco de 1.000.000: R$ {valor_investido_total}')
        print(f'Valor de dividendos recebidos: R$ {dividendos_recebidos}')
        print(f'Valor de juros compostos: R$ {juros_compostos}')
        return
    elif valor_investido_total >= 100000:
        print(f'Marca de R$ 100.000,00 atingida em {meses//12} anos e {meses%12} meses')
        print(f'Valor investido até o marco de 100.000: R$ {valor_investido_total}')
        print(f'Valor de dividendos recebidos: R$ {dividendos_recebidos}')
        print(f'Valor de juros compostos: R$ {juros_compostos}')
        return

    # Investimento de R$ 80,00 mensais
    investido += 80
    valor_investido_total += 80
    
    # Calcula o valor de dividendos com base nas ações
    dividendos = sum([acao['dividendo'] for acao in acoes])  # Somatório dos dividendos mensais
    dividendos_recebidos += dividendos

    # Calcula os juros compostos (utilizando uma taxa fictícia de 0.5% ao mês)
    taxa_juros = 0.005  # 0.5% ao mês
    juros_compostos += valor_investido_total * taxa_juros

    # Chama a função recursiva para o próximo mês
    investimento(investido, meses + 1, acoes, valor_investido_total + juros_compostos, dividendos_recebidos, juros_compostos)

# Parâmetros iniciais
investido = 0
meses = 0
valor_investido_total = 0
dividendos_recebidos = 0
juros_compostos = 0

# Chama a função recursiva para iniciar o investimento
investimento(investido, meses, acoes_2024, valor_investido_total, dividendos_recebidos, juros_compostos)