# Método Copy

contatos = {
    "guilherme@gmail.com": {
        "nome": "Guilherme",
        "telefone": "1234-5678"
    },

    "giovanna@gmail.com": {
        "nome": "Giovanna",
        "telefone": "8765-4321"
    },

    "chappie": {
        "nome": "Chappie",
        "telefone": "0000-0000"
    },
}

# Método COPY
print("Método Copy")
copia = contatos.copy()
print("Cópia dos contatos:", copia)
print()


print("==" * 20)