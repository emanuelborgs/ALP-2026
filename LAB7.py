
# Problema1:
# O contador nunca era tavntro do while,
# tinha um loop infinito
# Problema2:
#nao atualizava o contado e o progama nao terminava;)
N = int(input("Quantos números quer digitar? "))
contador = 1
impares = 0
while contador <= N:
    num = int(input("Digite um número: "))
    # olha se o numero e inpar
    if num % 2 != 0:
        impares += 1
    contador += 1
print(float'Quantidade de ímpares: {impares}')