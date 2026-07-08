def ola (nome):
    return f'ola {nome}'
genero= input("qual o seu genero")
nome= input("insira seu nome:")

if genero != masculino or genero != feminino or genero != neutro:
    print("coloca um genero decente")
else:
    print(f'ola {nome} seu genero e {genero}')