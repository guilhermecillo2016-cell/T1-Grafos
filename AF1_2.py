import sys
from A1_1 import Grafo_nao_dirigido_ponderado
def busca_em_largura(grafo, vertice_inicial):
    vizitados = set()
    vizitados.add(vertice_inicial)
    D = {}  # Dicionário para armazenar as distâncias
    D[vertice_inicial] = 0  # Distância do vértice inicial é 0
    lista_strings = []  # Lista para armazenar as strings de saída
    fila = [vertice_inicial]
    while fila:
        vertice_atual = fila.pop(0)
        lista_strings.insert(D[vertice_atual],str(vertice_atual) + ",")  # Insere o vértice na posição correspondente à sua distância
        for vizinho in grafo.vizinhos(vertice_atual):
            if vizinho not in vizitados:
                vizitados.add(vizinho)
                D[vizinho] = D[vertice_atual] + 1  # Atualiza a distância do vizinho
                fila.append(vizinho)
    for i in range(len(lista_strings)):
        print(f"{i}: {lista_strings[i]}")
grafo = Grafo_nao_dirigido_ponderado()
grafo.ler_arquivo("teste.txt")
busca_em_largura(grafo, 1)
