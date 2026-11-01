import sys
from A2_0 import Grafo
def kruskal (arquivo):
    grafo = Grafo()
    grafo.ler_arquivo(arquivo)
    # Inicializa a lista de arestas do grafo
    arestas = list(grafo.arestas.items())
    # Ordena as arestas pelo peso
    arestas.sort(key=lambda x: x[1])
    
    # Inicializa o conjunto de componentes conectados
    componentes = {v: v for v in grafo.vertices}
    
    def encontrar_componente(v):
        if componentes[v] != v:
            componentes[v] = encontrar_componente(componentes[v])
        return componentes[v]
    
    def unir_componentes(v1, v2):
        comp1 = encontrar_componente(v1)
        comp2 = encontrar_componente(v2)
        if comp1 != comp2:
            componentes[comp2] = comp1
    
    arvore_geradora_minima = []
    
    for (v1, v2), peso in arestas:
        if encontrar_componente(v1) != encontrar_componente(v2):
            arvore_geradora_minima.append((v1, v2, peso))
            unir_componentes(v1, v2)
    total_peso = sum(peso for _, _, peso in arvore_geradora_minima)
    print(round(total_peso, 1))
    frase = ""
    for v1, v2, peso in arvore_geradora_minima:
        frase += f"{v1}-{v2}, "
    print(frase[:-2])  # Remove a última vírgula e espaço
kruskal(sys.argv[1])
