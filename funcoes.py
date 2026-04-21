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

def calcula_pontos_sequencia_baixa(dados_cairam):
    dicio1 = {1 :0, 2:0, 3:0, 4:0}
    dicio2 = {2:0, 3:0, 4:0, 5:0}
    dicio3 = {3:0, 4:0, 5:0, 6:0}
    resposta = 15
    for numero in dados_cairam:
        if numero in dicio1:
            dicio1[numero] += 1
        if numero in dicio2:
            dicio2[numero] += 1
        if numero in dicio3:
            dicio3[numero] += 1
    
    for numero in dicio1:
        if dicio1[numero] == 0:
            for numero in dicio2:
                if dicio2[numero] == 0:
                    for numero in dicio3:
                        if dicio3[numero] == 0:
                            resposta = 0
    return resposta

    
def calcula_pontos_sequencia_alta  (lista_de_dados):
    dicio1 = {1:0, 2:0, 3:0, 4:0, 5:0}
    dicio2 = {2:0, 3:0, 4:0, 5:0, 6:0}
    for n in lista_de_dados:
        if n in dicio1:
            dicio1[n] += 1
        if n in dicio2:
            dicio2[n] += 1
    for value in dicio1.values():
        if value == 0:
            for v in dicio2.values():
                if v == 0:
                    return 0
    return 30

def calcula_pontos_full_house(dados):
    dicio = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0}
    for numero in dados:
        dicio[numero] += 1
    tem_trinca = False
    tem_par = False     
    for valor in dicio.values():
        if valor == 3:
            tem_trinca = True
        if valor == 2:
            tem_par = True
    lista_numeros_dicio = []
    for numero in dicio:
        if dicio[numero] == 2:
            lista_numeros_dicio.append(2*numero)
        elif dicio[numero] == 3:
            lista_numeros_dicio.append(3*numero)
    
    if tem_trinca and tem_par:
        soma = 0 
        for i in lista_numeros_dicio:
            soma += i
        return soma
    else:
        return 0