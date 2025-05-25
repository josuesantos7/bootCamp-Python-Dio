# Compressão de Listas:

# Versão tradicional
print("Versão tradicional")
numeros = [1,30,211,2,9,65,34]
pares = []

for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)

print(pares)

print("--" * 20)


# Versão com Compreensão de Listas
print("Versão com Compreensão de Listas")
pares = [numero for numero in numeros if numero % 2 == 0]
print(pares)