from funcoes import *

cartela = {
    'regra_simples':  {
        1:-1,
        2:-1,
        3:-1,
        4:-1,
        5:-1,
        6:-1
    },
    'regra_avancada' : {
        'sem_combinacao':-1,
        'quadra': -1,
        'full_house': -1,
        'sequencia_baixa': -1,
        'sequencia_alta': -1,
        'cinco_iguais': -1
    }
}

count = 0
pontuacao = 0
ponto_simples = 0
ponto_avancada = 0
bonus = 0
imprime_cartela(cartela)

while count < 12:
    dados_rolados = rolar_dados(5)
    dados_guardados = []
    rerrolagem = 0
    while True:
        print(f'Dados rolados: {dados_rolados}')
        print(f'Dados guardados: {dados_guardados}')
        print('Digite 1 para guardar um dado, 2 para remover um dado, 3 para rerrolar, 4 para ver a cartela ou 0 para marcar a pontuação:')

        while True:
            jogada = input()
            if jogada not in ('0','1','2','3','4'):
                print("Opção inválida. Tente novamente.")
                continue
            break

        if jogada == '1':
            print('Digite o índice do dado a ser guardado (0 a 4):')
            indice = int(input())
            if indice < len(dados_rolados):
                dados_rolados, dados_guardados = guardar_dado(dados_rolados, dados_guardados, indice)
                
        
        elif jogada == '2':
            print('Digite o índice do dado a ser removido (0 a 4):')
            indice_remove = int(input())
            if indice_remove < len(dados_guardados):
                dados_rolados, dados_guardados = remover_dado(dados_rolados, dados_guardados, indice_remove)
                

        elif jogada == '3':
            if rerrolagem == 2:
                print("Você já usou todas as rerrolagens.")
                continue
            else:
                rerrolagem += 1
                dados_rolados = rolar_dados(5-len(dados_guardados))
                continue
        
        elif jogada == '4':
            imprime_cartela(cartela)
            continue

        else:
            print('Digite a combinação desejada:')       
            total = dados_rolados + dados_guardados
            while True:
                combinacao = input()
                if combinacao.isdigit():
                    combinacao = int(combinacao)
                if combinacao not in cartela['regra_simples'] and combinacao not in cartela['regra_avancada']:
                    print("Combinação inválida. Tente novamente.")
                    continue
                if combinacao in cartela['regra_simples'] and cartela['regra_simples'][combinacao] != -1:
                    print('Essa combinação já foi utilizada.')
                    continue
                if combinacao in cartela['regra_avancada'] and cartela['regra_avancada'][combinacao] != -1:
                    print('Essa combinação já foi utilizada.')
                    continue
                break
            

            
            if combinacao in cartela['regra_simples'] and cartela['regra_simples'][combinacao] == -1:   
                pontos = calcula_pontos_regra_simples(total)
                cartela['regra_simples'][combinacao] = pontos[combinacao]

            elif combinacao in cartela['regra_avancada'] :

                if combinacao == 'sem_combinacao':
                    cartela['regra_avancada'][combinacao] = calcula_pontos_soma (total)

                elif combinacao == 'quadra' :
                    cartela['regra_avancada'][combinacao] = calcula_pontos_quadra(total)

                elif combinacao == 'full_house':
                    cartela['regra_avancada'][combinacao] = calcula_pontos_full_house(total)

                elif combinacao == 'sequencia_baixa':
                    cartela['regra_avancada'][combinacao] = calcula_pontos_sequencia_baixa(total)

                elif combinacao == 'sequencia_alta':
                    cartela['regra_avancada'][combinacao] = calcula_pontos_sequencia_alta(total)

                else:
                    cartela['regra_avancada'][combinacao] = calcula_pontos_quina(total)
            
            
            count += 1
            break

for regra, dados in cartela.items():
    if regra == 'regra_simples':
        for tipo, valor in dados.items():
            if valor != -1:
                ponto_simples += valor
    elif regra == 'regra_avancada':
        for tipo, valor in dados.items():
            if valor != -1:
                ponto_avancada += valor

if ponto_simples >= 63:
    bonus = 35

pontuacao = ponto_simples + ponto_avancada + bonus
imprime_cartela(cartela)
print(f"Pontuação total: {pontuacao}")




