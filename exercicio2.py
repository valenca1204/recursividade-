def soma_lista(list):
    soma = 0
    list = [1,2,3,4,5]
    for i in list:
        soma += i
        
    return soma

resultado = soma_lista([1, 2, 3, 4, 5])
print(resultado)
