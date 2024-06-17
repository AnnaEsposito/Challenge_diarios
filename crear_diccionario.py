claves = [1, 2, 3]
valores = ['Anna', 'gato', 'perro']


diccionario = dict(zip(claves, valores))

for clave, valor in diccionario.items():
    print(f'{clave}: {valor}')