
# Verifica se um ano é bissexto
def eh_bissexto(ano):
    """
    Verifica se o ano informado é bissexto.
    Retorna True se for bissexto e False caso contrário.
    """
    if ano % 400 == 0:
        return True
    elif ano % 100 == 0:
        return False
    elif ano % 4 == 0:
        return True
    else:
        return False


# Calcula o Índice de Massa Corporal (IMC)
def calcular_imc(peso, altura):
    """
    Calcula o IMC usando o peso em kg e a altura em metros.
    """
    imc = peso / (altura ** 2)
    return round(imc, 2)


# Testando a função de ano bissexto
print("=== TESTE DE ANOS BISSEXTOS ===")

print("Ano 2000:", eh_bissexto(2000))
print("Ano 1900:", eh_bissexto(1900))
print("Ano 2024:", eh_bissexto(2024))
print("Ano 2023:", eh_bissexto(2023))


# Testando a função de IMC
print("\n=== TESTE DE IMC ===")

resultado1 = calcular_imc(70, 1.75)
resultado2 = calcular_imc(85, 1.80)

print(f"Pessoa 1: IMC = {resultado1}")
print(f"Pessoa 2: IMC = {resultado2}")
