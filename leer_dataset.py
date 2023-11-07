import csv

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