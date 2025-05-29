# Issubset

conjunto_a = {1, 2, 3}
conjunto_b = {1, 2, 3, 4, 5}
conjunto_a.issubset(conjunto_b) # True
conjunto_b.issubset(conjunto_a) # False
print("Significa que todos os elementos do conjunto_a estão contidos no conjunto_b:", conjunto_a.issubset(conjunto_b))