# Método PopItem

print("Método PopItem")
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

contatos.popitem()
print("# Remove o último item adicionado")  
print(contatos)