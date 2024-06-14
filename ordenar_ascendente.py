

numeros = input("Ingresa una lista de números separados por comas: ")

lista_numeros = [int(num) for num in numeros.split(",")]

lista_numeros.sort()
print("Lista ordenada en orden ascendente:", lista_numeros)