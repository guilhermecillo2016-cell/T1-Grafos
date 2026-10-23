import sys
from A2_0 import Grafo
INF = float('inf')

def ordenacao_topologica(grafo: Grafo) -> list:
    visitados = set()
    T = {v: INF for v in grafo.vertices}
    F = {v: INF for v in grafo.vertices}

    tempo = 0
    O = []

    for v in grafo.vertices:
        if v not in visitados:
            tempo = DFS_visit_OT(grafo, v, visitados, T, F, tempo, O)
            
    return O

def DFS_visit_OT(grafo: Grafo, vertice: int, visitados: set, T: dict, F: dict, tempo: int, O: list) -> int:
    visitados.add(vertice)  # Correção: set usa .add()
    tempo += 1
    T[vertice] = tempo
    
    for u in grafo.vizinhos(vertice):
        if u not in visitados:
            tempo = DFS_visit_OT(grafo, u, visitados, T, F, tempo, O)
            
    tempo += 1
    F[vertice] = tempo
    
    O.insert(0, vertice) 
    
    return tempo

if __name__ == "__main__":
    arquivo = sys.argv[1]
    grafo = Grafo()
    grafo.ler_arquivo(arquivo)
    ordenados = ordenacao_topologica(grafo)

    nomes_ordenados = []
    for v in ordenados:
        rotulo = grafo.rotulo(v)
        rotulo = rotulo.replace('"', '')
        nomes_ordenados.append(rotulo)
    print(", ".join(nomes_ordenados))