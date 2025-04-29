# Conhecendo métodos da classe String:

# Maiúsculas:
curso = "pYtHon"
print(curso.upper())

# Minúsculas:
print(curso.lower())

# Titulo:
print(curso.title())


# Eliminando espaços em branco:
curso = "   Python   "
print(curso.strip())

print(curso.lstrip())

print(curso.rstrip())


# Junções e centralização:
curso = "Python"
print(curso.center(10, "#"))

print(".".join(curso))