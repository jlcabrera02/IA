matriz = [[0, 0, 8], [0, 0, 0], [0, 2, 0]]

# acumulador = 0

for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        if matriz[i][j] != 0:
            # acumulador += 1
            print(
                f"El numero diferentes a cero esta en el indice {j} del la lista con el indice {i}")
