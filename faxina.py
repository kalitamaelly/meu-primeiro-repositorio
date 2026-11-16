import csv
import re
from datetime import datetime

# Abre o arquivo original
with open("sujo.csv", "r", encoding="utf-8") as arquivo:
    leitor = csv.DictReader(arquivo)
     # Cria uma lista para armazenar os dados limpos
    dados_limpos = []

    # Percorre cada linha do arquivo
    for linha in leitor:

        # Padroniza o nome
        nome = linha["nome"].strip().title()
  # Remove tudo que não for número do telefone
        telefone = re.sub(r"\D", "", linha["telefone"])

        # Converte a data para o formato AAAA-MM-DD
        data = datetime.strptime(
            linha["data"].strip(), "%d/%m/%Y"
        ).strftime("%Y-%m-%d")

        # Verifica se o telefone possui 11 dígitos
        if re.fullmatch(r"\d{11}", telefone):
            status = "Válido"
        else:
            status = "Inválido"

        # Adiciona os dados tratados à lista
        dados_limpos.append({
            "nome": nome,
            "telefone": telefone,
            "data": data,
            "status": status
        })

# Cria o arquivo com os dados limpos
with open("limpo.csv", "w", newline="", encoding="utf-8") as arquivo:
    campos = ["nome", "telefone", "data", "status"]

    escritor = csv.DictWriter(arquivo, fieldnames=campos)

    # Escreve o cabeçalho
    escritor.writeheader()

    # Escreve os dados
    escritor.writerows(dados_limpos)

print("Limpeza concluída! Arquivo limpo.csv criado com sucesso.")
