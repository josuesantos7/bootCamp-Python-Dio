# Isdisjoint

conjunto_a = {1, 2, 3, 4, 5}
conjunto_b = {6, 7, 8, 9}
conjunto_c = {1, 0}


conjunto_a.isdisjoint(conjunto_b)  # True, porque não há elementos em comum
print("Conjunto A e B são disjuntos:", conjunto_a.isdisjoint(conjunto_b))
print("True, porque não há elementos em comum")

conjunto_a.isdisjoint(conjunto_c)  # False, porque há o elemento 1 em comum
print("Conjunto A e C não são disjuntos:", conjunto_a.isdisjoint(conjunto_c))
print("Falso, porque há elementos em comum")


