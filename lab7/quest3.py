
# Problema 1:
# A variável "soma" foi usada no while, mas ela nem existe.
# Problema 2:
# "maior" começou com float('inf'),
# que representa infinito positivo.
# Nenhum número digitado seria maior que isso.
# Correção:
# Começamos com um número muito pequeno
# ou usamos o primeiro valor digitado.
contador = 1
maior = float('-inf')
while contador <= 10:
    num = int(input("Digite um número: "))
    # Atualiza o maior número
    if num > maior:
        maior = num
    contador += 1
print("O maior número é", maior)