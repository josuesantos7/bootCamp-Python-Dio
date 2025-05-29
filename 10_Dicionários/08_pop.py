# Método pop

print("Método Pop")
contatos = {
    "guilherme@gmail.com": {
        "nome": "Guilherme",
        "telefone": "1234-5678"
    },
    "alexandra@gmail.com": {
        "nome": "Alexandra",
        "telefone": "8765-4321"
    },
}

print(contatos)
print()

print("Após o uso do método pop")
contatos.pop("guilherme@gmail.com")
print(contatos)