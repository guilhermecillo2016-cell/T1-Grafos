class Grafo_nao_dirigido_ponderado:
    def __init__(self):
        self.vertices = {}
        self.vizinhanca = {}
        self.arestas = {}
    def adicionar_vertice(self, vertice, rotulo):
        if vertice not in self.vertices:
            self.vertices[vertice] = rotulo
            self.vizinhanca[vertice] = []
    def adicionar_aresta(self, vertice1, vertice2, peso):
        if vertice1 in self.vertices and vertice2 in self.vertices:
            self.arestas[(vertice1, vertice2)] = peso
            self.vizinhanca[vertice1].append(vertice2)
            self.vizinhanca[vertice2].append(vertice1)
    def ler_arquivo(self, nome_arquivo):
        with open(nome_arquivo, 'r') as arquivo:
            primeira_linha = arquivo.readline().strip().split()
            v = int(primeira_linha[1])
            for i in range(v):
                linha = arquivo.readline().strip().split()
                self.adicionar_vertice(int(linha[0]), linha[1])
            next(arquivo)  # Pular a linha em branco
            for linha in arquivo:
                linha = linha.strip().split()
                self.adicionar_aresta(int(linha[0]), int(linha[1]), float(linha[2]))
    def quantidade_vertices(self):
        return len(self.vertices)
    def quantidade_arestas(self):
        return len(self.arestas)
    def grau(self, vertice):
        if vertice in self.vertices:
            return len(self.vizinhanca[vertice])
        else:
            return 0
    def rotulo(self, vertice):
        if vertice in self.vertices:
            return self.vertices[vertice]
        else:
            return None
    def vizinhos(self, vertice):
        if vertice in self.vertices:
            return self.vizinhanca[vertice]
        else:
            return []
    def ha_aresta(self, vertice1, vertice2):
        return (vertice1, vertice2) in self.arestas or (vertice2, vertice1) in self.arestas
    def peso(self, vertice1, vertice2):
        if self.ha_aresta(vertice1, vertice2):
            return self.arestas[(vertice1, vertice2)]
        else:
            return None
grafo = Grafo_nao_dirigido_ponderado()
grafo.ler_arquivo('blabla.txt')
print(grafo.rotulo(1))
print(grafo.vizinhos(1))