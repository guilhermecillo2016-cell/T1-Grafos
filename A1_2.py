from Grafo import Grafo_nao_dirigido_ponderado
from collections import deque, defaultdict

def busca_em_largura(arquivo, vertice_inicial):
    grafo = Grafo_nao_dirigido_ponderado()
    grafo.ler_arquivo(arquivo)
    visitados = set()
    visitados.add(vertice_inicial)
    niveis = defaultdict(list) #dicionario iniciado com listas vazias
    fila = deque([(vertice_inicial, 0)]) #fila com O(1) para retirar, armazenando tuplas
    while fila:
        vertice_atual, nivel = fila.popleft()
        niveis[nivel].append(vertice_atual)
        for vizinho in grafo.vizinhos(vertice_atual):
            if vizinho not in visitados:
                visitados.add(vizinho)
                fila.append((vizinho, nivel + 1))
    
    for key in niveis:
        print(f"{key}: ", end='')
        for i in range(len(niveis[key])):
            if i != len(niveis[key]) - 1:
                print(f"{niveis[key][i]},", end='')
            else:
                print(f"{niveis[key][i]}")
busca_em_largura("teste.txt", 1)
