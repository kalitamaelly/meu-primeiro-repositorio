def so_digitos(texto):
    return ''.join(caractere for caractere in texto if caractere.isdigit())

def normalizar_nome(nome):
    return nome.strip().title()

def formatar_data(texto):
    dia, mes, ano = texto.split("/")
    return f"{ano}-{mes}-{dia}"


if __name__ == "__main__":
    print(so_digitos("CPF: 123.456.789-00"))
    print(normalizar_nome("  kalita maelly  "))
    print(formatar_data("20/11/2026"))

