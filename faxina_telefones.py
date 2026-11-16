
import re
import csv

# Abre o arquivo de contatos
with open("contatos.csv", "r", encoding="utf-8") as arquivo:
    contatos = csv.DictReader(arquivo)

    # Percorre cada contato
    for contato in contatos:
        nome = contato["nome"]
        telefone = contato["telefone"]

        # Remove tudo que não for dígito
        telefone_limpo = re.sub(r"\D", "", telefone)

        # Verifica se possui exatamente 11 dígitos
        if re.fullmatch(r"\d{11}", telefone_limpo):
            status = "Válido"
        else:
            status = "Inválido"

        # Exibe o resultado
        print(f"{nome}: {telefone_limpo} - {status}")
