
numeros = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]

for i in range(len(numeros)):
    for j in range(0, len(numeros) - i - 1):
        if numeros[j] > numeros[j + 1]:
            # Intercambia los elementos
            numeros[j], numeros[j + 1] = numeros[j + 1], numeros[j]

print("Lista de números ordenada en orden ascendente:", numeros)