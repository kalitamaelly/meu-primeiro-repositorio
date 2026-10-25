with open("diario.txt", "w", encoding="utf-8") as arquivo:
    arquivo.write("Querido diário, hoje comecei a estudar python.\n")
    arquivo.write("Estou aprendendo programação.\n")
    arquivo.write("Quero melhorar todos os dias.\n")

with open("diario.txt", "a", encoding="utf-8") as arquivo:
        arquivo.write("Hoje pratiquei escrita em arquivos.\n")
        arquivo.write("Estou avançando nos meus estudos.\n")

with open("diario.txt", "r", encoding="utf-8") as arquivo:
    for numero, linha in enumerate(arquivo, start=1):
        print(f"{numero}.{linha.strip()}")


