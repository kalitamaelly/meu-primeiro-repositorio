
# Calcula a média de uma lista de notas
def media(notas):
    """
    Recebe uma lista de notas e retorna a média.
    """
    return sum(notas) / len(notas)


# Calcula o desconto de um produto
def desconto(preco, percentual=10):
    """
    Calcula o preço final após aplicar um desconto.
    O desconto padrão é de 10%.
    """
    valor_desconto = preco * (percentual / 100)
    return preco - valor_desconto


# Retorna o menor valor, maior valor e média das notas
def estatisticas(notas):
    """
    Retorna o mínimo, máximo e média de uma lista.
    """
    minimo = min(notas)
    maximo = max(notas)
    media_notas = media(notas)

    return minimo, maximo, media_notas


# Verifica a situação do aluno
def situacao(media):
    """
    Retorna Aprovado ou Reprovado conforme a média.
    """
    if media >= 7:
        return "Aprovado"
    else:
        return "Reprovado"


# TESTANDO AS FUNÇÕES

print("=== MÉDIA ===")

notas_aluno = [8, 7, 9, 10]
resultado_media = media(notas_aluno)
print(f"Média do aluno: {resultado_media:.2f}")


print("\n=== DESCONTO ===")

# Argumentos posicionais
preco1 = desconto(200, 20)

# Argumentos nomeados
preco2 = desconto(preco=150, percentual=15)

# Utilizando o percentual padrão de 10%
preco3 = desconto(100)

print(f"Produto 1: R$ {preco1:.2f}")
print(f"Produto 2: R$ {preco2:.2f}")
print(f"Produto 3: R$ {preco3:.2f}")


print("\n=== ESTATÍSTICAS ===")

menor, maior, media_notas = estatisticas(notas_aluno)

print(f"Menor nota: {menor}")
print(f"Maior nota: {maior}")
print(f"Média: {media_notas:.2f}")


print("\n=== SITUAÇÃO DO ALUNO ===")

resultado = situacao(resultado_media)
print(f"Situação: {resultado}")
