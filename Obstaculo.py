def add_or_sub(a, b):
    if b > a:
        a += 1
    elif b < a:
        a -= 1
    else:
        a
    return a


def recorrer(inicio, destino, matriz):
    (x_destino, y_destino), (x_inicio, y_inicio) = destino, inicio
    while x_destino != x_inicio:
        x_inicio = add_or_sub(x_inicio, x_destino)
        if matriz[y_inicio][x_inicio] == 1:
            x_inicio = add_or_sub(x_inicio, y_inicio)
            break
        coor.append([x_inicio, y_inicio])

    while y_destino != y_inicio:
        y_inicio = add_or_sub(y_inicio, y_destino)
        if matriz[y_inicio][x_inicio] == 1:
            y_inicio = add_or_sub(y_inicio, x_inicio)
            break
        coor.append([x_inicio, y_inicio])

    if (x_destino != x_inicio or y_destino != y_inicio):
        recorrer([x_inicio, y_inicio], [x_destino, y_destino], matriz)


matriz = [
    [2, 0, 0, 1, 0],
    [1, 0, 0, 0, 3],
    [0, 1, 0, 1, 0],
    [0, 1, 0, 0, 0],
    [0, 0, 1, 0, 0]
]

for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        if matriz[i][j] == 2:
            coor = [[j, i]]
        if matriz[i][j] == 3:
            coor2 = [j, i]

recorrer(coor[0],  coor2, matriz)

print(f"Numero de pasos a reccorridos: {len(coor)-1}")
for x, y in coor:
    print(f"({y}, {x})")
