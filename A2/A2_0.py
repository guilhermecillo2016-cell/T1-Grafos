import sys
class Grafo:
    def __init__(self, dirigido=False):
        self.vertices = {}
        self.vizinhanca = {}
        self.arestas = {}
        self.dirigido = dirigido
    def adicionar_vertice(self, vertice, rotulo):
        if vertice not in self.vertices:
            self.vertices[vertice] = rotulo
            self.vizinhanca[vertice] = []
    def adicionar_aresta(self, vertice1, vertice2, peso):
        if vertice1 in self.vertices and vertice2 in self.vertices:
            self.arestas[(vertice1, vertice2)] = peso
            self.vizinhanca[vertice1].append(vertice2)
            if not self.dirigido:
                self.vizinhanca[vertice2].append(vertice1)
    def ler_arquivo(self, nome_arquivo):
        with open(nome_arquivo, 'r') as arquivo:
            linhas = arquivo.read().strip().split('\n')
            
            lendo_vertices = False
            lendo_arestas = False
            
            for linha in linhas:
                linha = linha.strip()
                if not linha:
                    continue
                
                if linha.startswith('*vertices'):
                    lendo_vertices = True
                    lendo_arestas = False
                    continue
                elif linha.startswith('*edges') or linha.startswith('*arcs'):
                    lendo_vertices = False
                    lendo_arestas = True
                    # Se for *arcs, define a classe como dirigida automaticamente
                    if linha.startswith('*arcs'):
                        self.dirigido = True
                    continue
                
                if lendo_vertices:
                    # Formato: "1 rotulo_de_1"
                    partes = linha.split(maxsplit=1)
                    indice = int(partes[0])
                    rotulo = partes[1] if len(partes) > 1 else ""
                    self.adicionar_vertice(indice, rotulo)
                    
                elif lendo_arestas:
                    # Formato: "a b valor_do_peso"
                    partes = linha.split()
                    if len(partes) >= 3:
                        v1 = int(partes[0])
                        v2 = int(partes[1])
                        peso = float(partes[2])
                        self.adicionar_aresta(v1, v2, peso)
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
        if (vertice1, vertice2) in self.arestas:
            return self.arestas[(vertice1, vertice2)]
        elif (vertice2, vertice1) in self.arestas:
            return self.arestas[(vertice2, vertice1)]
        else:
            return sys.float_info.max