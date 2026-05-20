

import random
numero_secreto = random.randint(1, 10)
chances = 5
while chances > 0:
    palpite = int(input(f"Digite um número de 1 a 10 ({chances} chances): "))
    if palpite == numero_secreto:
        print("Parabéns! Você acertou o número!")
        break
    else:
        print("Número incorreto.")
        chances -= 1
if chances == 0 and palpite != numero_secreto:
    print(f"Você perdeu! O número era {numero_secreto}")