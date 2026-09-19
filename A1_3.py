from Grafo import Grafo_nao_dirigido_ponderado
"""
Este programa verifica se há um Ciclo Euleriano no Grafo. A função deve receber o grafo como argumento.
Deve retornar 1 na primeira linha se houver ciclo e 0 caso contrário. Além disso, deve retornar o caminho
de vértices que compõe o ciclo.
"""

def BuscaCicloEuleriano(arquivo : str):
    grafo = Grafo_nao_dirigido_ponderado()
    grafo.ler_arquivo(arquivo)
    ciclo = []
    if grafo.quantidade_arestas() == 0:
        ciclo.append(list(grafo.vertices.keys())[0])

    caminhoAtual = []
    caminhoAtual.append(list(grafo.vertices.keys())[0])

    while caminhoAtual:
        vertice_atual = caminhoAtual[-1]

        if grafo.vizinhanca[vertice_atual]:
            proximo_vertice = grafo.vizinhanca[vertice_atual].pop()
            grafo.vizinhanca[proximo_vertice].remove(vertice_atual)
            caminhoAtual.append(proximo_vertice)
        else:
            ciclo.append(caminhoAtual.pop())
    
    if ciclo:
        print("1")
        print(",".join(map(str, ciclo)))
    else:
        print("0")

BuscaCicloEuleriano("teste1.txt")
