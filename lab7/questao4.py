

palavra_secreta = 'batata'
while chances > 0:
    palavra = input(f"Qual a palavra secreta? Você tem {chances} chances: ")
    chances -= 1
    if palavra == palavra_secreta:
        print("Você acertou a palavra, toma aqui uma batata 🥔")
        break
    else:
        print("Palavra incorreta! Tente novamente.")
if chances == 0 and palavra != palavra_secreta:
    print("Suas chances acabaram!")