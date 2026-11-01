import sys
from A2_0 import Grafo

def componentes_fortemente_conexas(arquivo: str):
    grafo = Grafo(dirigido=True)
    grafo.ler_arquivo(arquivo)

    visitado = set()
    F = []
    for r in sorted(grafo.vertices):
        if r in visitado:
            continue
        visitado.add(r)
        pilha = [(r, iter(grafo.vizinhos(r)))]
        while pilha:
            v, it = pilha[-1]
            for w in it:
                if w not in visitado:
                    visitado.add(w)
                    pilha.append((w, iter(grafo.vizinhos(w))))
                    break
            else:
                pilha.pop()
                F.append(v)
    F.reverse()

    entrada = {v: [] for v in grafo.vertices}
    for (a, b) in grafo.arestas:
        entrada[b].append(a)

    visitado = set()
    for r in F:
        if r in visitado:
            continue
        visitado.add(r)
        componente = []
        pilha = [r]
        while pilha:
            v = pilha.pop()
            componente.append(v)
            for w in entrada[v]:
                if w not in visitado:
                    visitado.add(w)
                    pilha.append(w)
        print(','.join(map(str, sorted(componente))))

componentes_fortemente_conexas(sys.argv[1])
