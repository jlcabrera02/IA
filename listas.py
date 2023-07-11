matriz = [
    [2, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 3],
    [0, 0, 0, 0, 0]
]

for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        if matriz[i][j] == 2:
            indice_2 = [i, j]
        if matriz[i][j] == 3:
            indice_3 = [i, j]

print(indice_2, indice_3)
numero_mov = ((indice_3[1] - indice_2[1])) + ((indice_3[0] - indice_2[0]))
print(numero_mov)
