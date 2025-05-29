# Metodo Del

print("Método Del")
contatos = {
    "guilherme@gmail.com": {
        "nome": "Guilherme",
        "telefone": "1234-5678"
    },
    "alexandra@gmail.com": {
        "nome": "Alexandra",
        "telefone": "8765-4321"
    },
    "jessica@gmail.com": {
        "nome": "Jessica",
        "telefone": "8765-4323"
    },
}

del contatos["guilherme@gmail.com"]
print(contatos)