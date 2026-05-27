
# Problema:
# O while usava "soma <= 10", mas soma representa
# o valor acumulado e não a quantidade de números digitados.
# Assim, o programa poderia parar antes ou continuar demais.
soma = 0
contador = 1
while contador <= 10:
    num = int(input("Digite um número para somar: "))
    soma += num
    contador += 1
print("Soma total =", soma)