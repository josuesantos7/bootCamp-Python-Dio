# Método Update

print("Método Update")

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

print("antes do uso do método update")
print(contatos)
print()


contatos.update({"guilherme@gmail.com": {
    "nome": "Guizera",}
    })

print("Após o uso do método update")
print(contatos)