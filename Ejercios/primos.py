cantidad = int(
    input("Digita hasta que número quieres ver los numeros primos: "))
numerosPrimos = []

for i in range(1, cantidad+1):
    numero = i
    for j in range(2, i):
        if (i % j) == 0:
            numero = False
    if numero:
        numerosPrimos.append(numero)

print(numerosPrimos)
