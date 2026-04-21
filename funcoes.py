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

def remover_dado(dados_rolados, dados_no_estoque, dado_para_remover) :
    dados_rolados.append(dados_no_estoque[dado_para_remover])
    del dados_no_estoque[dado_para_remover]
    
    return [dados_rolados, dados_no_estoque]

def calcula_pontos_regra_simples(dados_rolados):
    resposta = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}
    for i in range(len(dados_rolados)):
        resposta[dados_rolados[i]] += dados_rolados[i]
    return resposta

def calcula_pontos_soma  (lista_de_dados):
    soma = 0
    for n in lista_de_dados:
        soma += n
    return soma