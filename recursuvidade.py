# def fatorial(n):
#     if n == 0 or n == 1:
#         return 1
#     else:
#         return n * fatorial(n-1)
# n = int(input("digite um úmero inteiro positivo para descobrir o seu fatorial:"))
# print(fatorial(n))




# def soma_lista(list):
#     soma = 0
#     list = [1,2,3,4,5]
#     for i in list:
#         soma += i
        
#     return soma

# resultado = soma_lista([1, 2, 3, 4, 5])
# print(resultado)





# def inverter(str):
#     if len(str) <= 1:
#         return str
#     else:
#         return str[-1] + inverter(str[:-1])
    
# str = "pedro"
# print(inverter(str))



# def simulação(investimento):
#     saldo = 0
#     mes = 0
#     investido = 0 
#     juros = 0

#     investimento_mensal = investimento 
#     rendimento_mensal = 0.0005


#     while saldo < 1000000:

#         saldo += investimento_mensal
#         investido += investimento_mensal

#         saldo *= (1 + rendimento_mensal)

#         mes += 1



#         if saldo >= 100000 and juros == 0:
#             juros = saldo - investido  
#             anos100mil, meses100mil = divmod(mes, 12)  
#             print(f"Tempo para atingir R$ 100.000,00: {anos100mil} anos e {meses100mil} meses")
#             print(f"Valor investido até R$ 100.000,00: R$ {investido:.2f}")
#             print(f"Juros compostos até R$ 100.000,00: R$ {juros:.2f}\n")



#     anos_final, meses_final = divmod(mes, 12)  
#     juros_final = saldo - investido  
    
#     print(f"Tempo total para atingir R$ 1.000.000,00: {anos_final} anos e {meses_final} meses")
#     print(f"Valor investido até R$ 1.000.000,00: R$ {investido:.2f}")
#     print(f"Juros compostos totais: R$ {juros_final:.2f}")

# simulação(500)  




# import sys
# sys.setrecursionlimit(20000)  # Aumenta o limite de recursão para evitar erro

# def simulacao(valor_mensal, saldo=0, mes=0, investido=0, juros=0):
#     if saldo >= 1000000:
#         print(f"R$ 1.000.000,00 em {mes // 12} anos e {mes % 12} meses! Investido: R$ {investido:.2f}, Juros: R$ {saldo - investido:.2f}\n")
#         return
    
#     rendimento_mensal = 0.0005
#     saldo += valor_mensal
#     investido += valor_mensal
#     saldo *= (1 + rendimento_mensal)
#     mes += 1
    
#     if saldo >= 100000 and juros == 0:
#         juros = saldo - investido
#         print(f"R$ 100.000,00 em {mes // 12} anos e {mes % 12} meses! Investido: R$ {investido:.2f}, Juros: R$ {juros:.2f}\n")
    
#     simulacao(valor_mensal, saldo, mes, investido, juros)

# simulacao(500)






# cotacoes_btc_2024 = [
#     467506.83, 475000, 482000, 490000, 495000, 510000, 520000, 530000, 540000, 550000, 560000, 570000
# ]

# # Função recursiva para calcular os marcos de investimento
# def investimento(investido, meses, cotacoes_btc, valor_investido_total):
#     # Verifica se atingiu os marcos
#     if valor_investido_total >= 100000 and investido >= 100000:
#         print(f'Marca de R$ 100.000,00 atingida em {meses//12} anos e {meses%12} meses')
#         print(f'Valor investido até o marco de 100.000: R$ {valor_investido_total}')
#         return
#     elif valor_investido_total >= 1000000 and investido >= 1000000:
#         print(f'Marca de R$ 1.000.000,00 atingida em {meses//12} anos e {meses%12} meses')
#         print(f'Valor investido até o marco de 1.000.000: R$ {valor_investido_total}')
#         return
#     elif valor_investido_total >= cotacoes_btc[meses % 12] and investido >= cotacoes_btc[meses % 12]:
#         print(f'Marca de 1 Bitcoin atingida em {meses//12} anos e {meses%12} meses')
#         print(f'Valor investido até o marco de 1 Bitcoin: R$ {valor_investido_total}')
#         return

#     # Atualiza o valor investido mensalmente
#     investido += 250
#     valor_investido_total += 250
    
#     # Chama a função recursiva para o próximo mês
#     investimento(investido, meses + 1, cotacoes_btc, valor_investido_total)

# # Parâmetros iniciais
# investido = 0
# meses = 0
# valor_investido_total = 0

# # Chama a função recursiva para iniciar o investimento
# investimento(investido, meses, cotacoes_btc_2024, valor_investido_total)






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