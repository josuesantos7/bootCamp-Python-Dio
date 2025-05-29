# Método GET
print("Método Get")
contatos = {
    "guilherme@gmail.com": {
        "nome": "Guilherme",
        "telefone": "1234-5678"
    },
}

print("Contato de Guilherme:", contatos.get("guilherme", {}))