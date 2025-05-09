# Parâmetros especiais

# def exemplo_criar_carro(pos, pos, posi, /, posi_or_kwd, * kwd1, kwd2):
# posi = parametro de posicao obrigatorio.

def criar_carro(modelo, ano, placa, /, marca, motor, combustivel):
    print(modelo, ano, placa, marca, motor, combustivel)

criar_carro('Fusca', 1970, 'ABC-1234', marca='Volkswagen', motor='1.0', combustivel='Gasolina')