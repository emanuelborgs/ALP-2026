while True:
    resposta = input("Deseja continuar? (s/n): ")sss
    resposta = resposta.strip().lower()
    if resposta in ["s", "sim"]:
        continue
    elif resposta in ["n", "não", "nao"]:
        print("Obrigado! Encerrando o programa.")
        break
    else:
        print("Resposta inválida! Tente novamente.")