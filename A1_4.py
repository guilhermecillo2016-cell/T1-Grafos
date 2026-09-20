from A1_1 import Grafo_nao_dirigido_ponderado
import sys
INF = float('inf')


def reconstruir_caminho(A: dict, s: int, destino: int) -> list:
    caminho = []
    atual = destino
    while atual is not None:
        caminho.append(atual)
        if atual == s:
            break
        atual = A[atual]
    caminho.reverse()
    return caminho


def bellman_ford(arquivo: str, s: int):
    grafo = Grafo_nao_dirigido_ponderado()
    grafo.ler_arquivo(arquivo)

    #escolha de dicionario, pois nem sempre os vertices serão indices certos de uma lista (posso ter vertices = [0, 3 ,18 , 6])
    D = {v: INF for v in grafo.vertices}
    A = {v: None for v in grafo.vertices}
    D[s] = 0

    n = grafo.quantidade_vertices()

    for _ in range(n - 1):
        atualizou = False
        for (u, v), peso in grafo.arestas.items():
            if D[u] + peso < D[v]:
                D[v] = D[u] + peso
                A[v] = u
                atualizou = True
            if D[v] + peso < D[u]:
                D[u] = D[v] + peso
                A[u] = v
                atualizou = True
        if not atualizou:
            break  

    #detecta ciclo
    for (u, v), peso in grafo.arestas.items():
        if D[u] + peso < D[v] or D[v] + peso < D[u]:
            return

    for vertice in grafo.vertices:
        caminho = reconstruir_caminho(A, s, vertice)
        print(f"{vertice}: {','.join(map(str, caminho))}; d={int(D[vertice])}")


bellman_ford(sys.argv[1], int(sys.argv[2]))