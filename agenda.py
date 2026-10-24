contatos = [
    {"nome": "Ana", "telefone": "48999990001"},
    {"nome": "Bruno", "telefone": "48999990002"},
    {"nome": "Carla", "telefone": "48999990003"},
    {"nome": "Daniel", "telefone": "48999990004"},
    {"nome": "Eduarda", "telefone": "48999990005"}
]

def buscar_contato(nome):
    for contato in contatos:
        if contato["nome"].lower() == nome.lower():
            print("Nome:", contato["nome"])
            print("Telefone:", contato["telefone"])
            return
    print("Contato não encontrado.")

buscar_contato("Carla")
                