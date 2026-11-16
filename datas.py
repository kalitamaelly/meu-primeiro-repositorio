
from datetime import datetime, date

# Solicita a data de nascimento
nascimento_texto = input("Digite sua data de nascimento (dd/mm/aaaa): ")

# Converte o texto para uma data
nascimento = datetime.strptime(nascimento_texto, "%d/%m/%Y").date()

# Obtém a data atual
hoje = date.today()

# Calcula os dias vividos
dias_vividos = (hoje - nascimento).days

# Calcula a idade aproximada
idade = dias_vividos // 365

# Identifica o dia da semana em que nasceu
dias_semana = [
    "segunda-feira",
    "terça-feira",
    "quarta-feira",
    "quinta-feira",
    "sexta-feira",
    "sábado",
    "domingo"
]

dia_nascimento = dias_semana[nascimento.weekday()]

# Calcula quantos dias faltam para o próximo Natal
ano_natal = hoje.year

proximo_natal = date(ano_natal, 12, 25)

if proximo_natal <= hoje:
    proximo_natal = date(ano_natal + 1, 12, 25)

dias_para_natal = (proximo_natal - hoje).days

# Exibe os resultados
print("\n--- RESULTADO ---")
print(f"Você tem aproximadamente {idade} anos.")
print(f"Você nasceu em uma {dia_nascimento}.")
print(f"Faltam {dias_para_natal} dias para o próximo Natal!")
