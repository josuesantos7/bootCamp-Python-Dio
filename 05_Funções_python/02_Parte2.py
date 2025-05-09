# Parâmetros especiais

# def exemplo_criar_carro(pos, pos, posi, /, posi_or_kwd, * kwd1, kwd2):
# posi = parametro de posicao obrigatorio.

def criar_carro(modelo, ano, placa, /, marca, motor, combustivel):
    print(modelo, ano, placa, marca, motor, combustivel)

criar_carro('Fusca', 1970, 'ABC-1234', marca='Volkswagen', motor='1.0', combustivel='Gasolina')

print('---' * 10)
# Parametros nomeados (Keyword-only arguments)
def criar_carro2(*, modelo, ano, placa, marca, motor, combustivel):
    print(modelo, ano, placa, marca, motor, combustivel)

criar_carro2(modelo='Jetta', ano=2025, placa='ABC-1234', marca='Volkswagen', motor='2.0', combustivel='Gasolina')


print('---' * 10)
# Parametros variaveis hibridos(args e kwargs)
def criar_carro3(modelo, ano, placa, /, *, marca, motor, combustivel):
    print(modelo, ano, placa, marca, motor, combustivel)

criar_carro3('Jetta', 2025, 'ABC-1234', marca='Volkswagen', motor='2.0', combustivel='Gasolina')