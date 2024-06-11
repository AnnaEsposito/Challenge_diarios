# Solicitamos al usuario que ingrese una cadena
cadena = input("Ingrese una cadena de caracteres: ")

# Inicializamos una cadena vacía donde guardamos la cadena invertida
cadena_invertida = ""

# Iterar sobre la cadena de entrada en orden inverso y construir la cadena invertida
for caracter in reversed(cadena):
    cadena_invertida += caracter

print("La cadena invertida es:", cadena_invertida)
