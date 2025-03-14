
import sys

sys.setrecursionlimit(2000)


def simulação_recursiva(investimento, saldo, mes, investido, juros, preço_do_dolar):
    # Condição de parada: quando o saldo atingir R$ 1.000.000
    if saldo >= 1000000:
        anos_final, meses_final = divmod(mes, 12)
        juros_final = saldo - investido
        saldo_dolar = saldo / preço_do_dolar[mes % 12]
        
        print(f"\nTempo total para atingir R$ 1.000.000,00: {anos_final} anos e {meses_final} meses")
        print(f"Valor investido até R$ 1.000.000,00: R$ {investido:.2f}")
        print(f"Juros compostos totais: R$ {juros_final:.2f}")
        print(f"Investido total em dólares: USD {investido / preço_do_dolar[mes % 12]:.2f}")
        print(f"Saldo final em dólares: USD {saldo_dolar:.2f}")
        return  # A recursão termina aqui

    # Conversão para dólares
    investimento_dolar = investimento / preço_do_dolar[mes % 12]

    # Atualiza saldo e o valor investido
    saldo += investimento
    investido += investimento
    saldo *= (1 + 0.0005)  # Rendimento mensal de 0.05%
    mes += 1  # Incrementa o mês

    # Verifica quando atingir R$ 100.000
    if saldo >= 100000 and juros == 0:
        juros = saldo - investido
        anos100mil, meses100mil = divmod(mes, 12)
        print(f"Tempo para atingir R$ 100.000,00: {anos100mil} anos e {meses100mil} meses")
        print(f"Valor investido até R$ 100.000,00: R$ {investido:.2f}")
        print(f"Juros compostos até R$ 100.000,00: R$ {juros:.2f}")
        print(f"Investido até R$ 100.000,00 em dólares: USD {investido / preço_do_dolar[mes % 12]:.2f}")
        print(f"Saldo em dólares até R$ 100.000,00: USD {saldo / preço_do_dolar[mes % 12]:.2f}\n")

    # Chamada recursiva para o próximo mês, passando os parâmetros atualizados
    return simulação_recursiva(investimento, saldo, mes, investido, juros, preço_do_dolar)

# Parâmetros iniciais
preço_do_dolar = [4.87, 4.97, 4.98, 5.07, 5.07, 5.34, 5.46, 5.73, 5.60, 5.46, 5.74, 6.09]  # Cotação do dólar por mês
investimento_mensal = 500  # Investimento mensal em reais

# Chamada inicial da função recursiva
simulação_recursiva(investimento_mensal, saldo=0, mes=0, investido=0, juros=0, preço_do_dolar=preço_do_dolar)