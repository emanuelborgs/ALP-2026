import random
import time
while True:
    continuar = input("Deseja fazer uma pergunta? (s/n): ")
    continuar = continuar.strip().lower()
    if continuar in ["n", "não", "nao"]:
        print("Até a próxima... 🔮")
        break
    elif continuar not in ["s", "sim"]:
        print("Resposta inválida!")
        continue
    pergunta = input("Faça sua pergunta: ")
    print("Pensando")
    time.sleep(1)
    print("Consultando os mistérios do universo...")
    time.sleep(2)
    print("A resposta está se revelando...")
    time.sleep(2)
    prob = random.randint(1, 10)
    if prob <= 5:
        resposta = "SIM"
    else:
        resposta = "NÃO"
    print("🔮 Resposta:", resposta)