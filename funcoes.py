import random
def rolar_dados (dados):
    sorteio = []
    while len(sorteio) < dados:
        sorteado = random.randint(1, 6)
        sorteio.append(sorteado)
    return sorteio

def guardar_dado(dados_rolados, dados_guardados, indice_dado):
    novos_rolados = []
    novos_guardados = []
    for x in dados_guardados:
        novos_guardados.append(x)
    
    novos_guardados.append(dados_rolados[indice_dado])
    
    for i in range(len(dados_rolados)):
        if i != indice_dado:
            novos_rolados.append(dados_rolados[i])
    
    return [novos_rolados, novos_guardados]