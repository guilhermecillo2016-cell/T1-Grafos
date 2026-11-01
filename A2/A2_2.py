import sys
from A2_0 import Grafo
INF = float('inf')

def ordenacao_topologica(grafo: Grafo) -> list:
    visitados = set()
  
    O = []

    for v in grafo.vertices:
        if v not in visitados:
            DFS_visit_OT(grafo, v, visitados, O)
            
    return O

def DFS_visit_OT(grafo: Grafo, vertice: int, visitados: set, O: list):
    visitados.add(vertice)  
    
    for u in grafo.vizinhos(vertice):
        if u not in visitados:
            DFS_visit_OT(grafo, u, visitados, O)
    
    
    O.insert(0, vertice) 

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