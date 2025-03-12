def fatorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fatorial(n-1)
n = int(input("digite um úmero inteiro positivo para descobrir o seu fatorial:"))
print(fatorial(n))




def soma_lista(lista):
    