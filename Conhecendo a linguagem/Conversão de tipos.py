# Conversão de tipos:

# Inteiro para float:
preco = 10
print(preco)

preco = float(preco)
print(preco)


# Float para inteiro:
preco = 10.30
print(preco)

preco = int(preco)
print(preco)


# número para string:
preco = 10.50
idade = 28

print(str(preco))

print(type(str(idade)))

texto = f"idade {idade} e preço {preco}"
print(texto)


# string para número:
preco = "10.50"
idade = "28"

print(float(preco))
print(int(idade))

# obs: divisão com // significa divisão inteira, ou seja, o resultado é arredondado para baixo.