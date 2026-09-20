import sys
from A1_1 import Grafo_nao_dirigido_ponderado

INF = float('inf')

def floyd_warshall(arquivo: str):
    grafo = Grafo_nao_dirigido_ponderado()
    grafo.ler_arquivo(arquivo)

    n = grafo.quantidade_vertices()
    vertices = list(grafo.vertices.keys())
    idx = {v: i for i, v in enumerate(vertices)}

    D = [[0]*n for _ in range(n)]

    for u in vertices:
        for v in vertices:
            if u == v:
                D[idx[u]][idx[v]] = 0
            elif grafo.ha_aresta(u, v):
                D[idx[u]][idx[v]] = int(grafo.peso(u, v))
            else:
                D[idx[u]][idx[v]] = INF

    for k in vertices:
        for u in vertices:
            for v in vertices:
                D[idx[u]][idx[v]] = min(D[idx[u]][idx[v]], D[idx[u]][idx[k]] + D[idx[k]][idx[v]])

    for vertice in vertices:
        print(f"{vertice}: {','.join(map(str, D[idx[vertice]]))}")

floyd_warshall(sys.argv[1])