import random
def rolar_dados (dados):
    sorteio = []
    while len(sorteio) < dados:
        sorteado = random.randint(1, 6)
        sorteio.append(sorteado)
    return sorteio

