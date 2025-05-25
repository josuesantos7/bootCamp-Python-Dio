# Tuplas
# A tupla é uma coleção de objetos ordenados e imutáveis. As tuplas são semelhantes às listas, mas diferentemente das listas, as tuplas não podem ser modificadas após a sua criação. Elas são definidas usando parênteses `()`.

# obs: usasse o Tuple ou "," no final do ultimo elemento.
frutas = ("laranja", "maca", "uva",)

letras = tuple("python")

numeros = tuple([1, 2, 3, 4,])

pais = ("Brasil",)

# Tuplas alinhadas
print("Tuplas alinhadas:")
matriz = (
    (1, "a", 2),
    ("b", 3, 4),
    (6, 5, "c"),
)

print(matriz[0])
print(matriz[0][0])
print(matriz[0][-1])
print(matriz[-1][-1])


# Métodos da classe tupla:
print("Métodos da classe tupla:")

# .count() - Retorna o número de vezes que um valor aparece na tupla
print(".count():")
tupla = (1, 2, 3, 2, 25)
contagem = tupla.count(2)
print(f"O número de vezes que o valor 2 aparece na tupla é: {contagem}.")
print()


# .index() - Retorna o índice do primeiro elemento com o valor especificado
print(".index():")
tupla = (1, 2, 3, 2, 25)
indice = tupla.index(2)
print(f"O índice do primeiro elemento com o valor 2 é: {indice}.")
print()