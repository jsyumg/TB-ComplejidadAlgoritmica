import heapq
import csv

# MST Algoritmo Prim
def prim(G):
    n = len(G)
    visited = [False] * n
    g = [float('inf')] * n
    mst = []

    pq = []
    heapq.heappush(pq, (0, 0, -1))  # (g(s), s, parent)

    while pq:
        _, u, parent = heapq.heappop(pq)

        if not visited[u]:
            visited[u] = True

            if parent != -1:
                mst.append((parent, u, _))

            for v, w in G[u]:
                if not visited[v] and w < g[v]:
                    g[v] = w
                    heapq.heappush(pq, (w, v, u))

    return mst


# MST Algoritmo Kruskal
def find(parent, a):
    if parent[a] != a:
        parent[a] = find(parent, parent[a])
    return parent[a]

def union(parent, a, b):
    parentA = find(parent, a)
    parentB = find(parent, b)
    parent[parentA] = parentB


def kruskal(G):
    n = len(G)
    aristas = []
    for u in range(n):
        for v, w in G[u]:
            aristas.append((w, u, v))

    aristas.sort() # ordenarlos ascendente
    parent = [i for i in range(n)]
    mst = []

    for w, u, v in aristas:
        if find(parent, u) != find(parent, v):
            union(parent, u, v)
            mst.append((u, v, w))

    return mst

def construir_grafo(ruta):
    grafo = {} # diccionario para almacenar grafo (lista de adyacencia)
    with open(ruta, "r") as file:
        read = csv.DictReader(file)
        print("Leyendo archivo...")
        for col in read:
            nodo1 = int(col["Nodo1"])
            nodo2 = int(col["Nodo2"])
            datos_arista = eval(col["Datos"])
            latencia = datos_arista['latencia']

            # crear lista de aristas para cada nuevo nodo
            if nodo1 not in grafo:
                grafo[nodo1] = list()
            if nodo2 not in grafo:
                grafo[nodo2] = list()
            
            # se guarda las aristas para ambos nodos al ser un grafo no digirido
            grafo[nodo1].append((nodo2, latencia))
            grafo[nodo2].append((nodo1, latencia))
    
    return grafo

G = construir_grafo("datasets/aristas.csv")

# Impresión de ejemplo (primeras 10 aristas del nodo 0):
for i in range(10):
    print(G[0][i])

