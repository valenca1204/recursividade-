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



def simulação(investimento):
    saldo = 0
    mes = 0
    investido = 0 
    juros = 0

    investimento_mensal = investimento 
    rendimento_mensal = 0.0005


    while saldo < 1000000:

        saldo += investimento_mensal
        investido += investimento_mensal

        saldo *= (1 + rendimento_mensal)

        mes += 1



        if saldo >= 100000 and juros == 0:
            juros = saldo - investido  
            anos100mil, meses100mil = divmod(mes, 12)  
            print(f"Tempo para atingir R$ 100.000,00: {anos100mil} anos e {meses100mil} meses")
            print(f"Valor investido até R$ 100.000,00: R$ {investido:.2f}")
            print(f"Juros compostos até R$ 100.000,00: R$ {juros:.2f}\n")



    anos_final, meses_final = divmod(mes, 12)  
    juros_final = saldo - investido  
    
    print(f"Tempo total para atingir R$ 1.000.000,00: {anos_final} anos e {meses_final} meses")
    print(f"Valor investido até R$ 1.000.000,00: R$ {investido:.2f}")
    print(f"Juros compostos totais: R$ {juros_final:.2f}")

simulação(500)  

