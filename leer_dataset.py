import csv

# diccionario para almacenar grafo
grafo = {}

# cargar los nodos
with open("datasets/nodos.csv", "r") as nodos_file:
    nodos_reader = csv.DictReader(nodos_file)
    for row in nodos_reader:
        nodo_id = int(row["Nodo"])
        datos_nodo = eval(row["Datos"])
        grafo[nodo_id] = {"datos": datos_nodo, "aristas": {}} # guarda los datos del nodo y aristas

# cargar las aristas
with open("datasets/aristas.csv", "r") as aristas_file:
    aristas_reader = csv.DictReader(aristas_file)
    for row in aristas_reader:
        nodo1 = int(row["Nodo1"])
        nodo2 = int(row["Nodo2"])
        datos_arista = eval(row["Datos"]) # la latencia almacenada en la arista

        grafo[nodo1]["aristas"][nodo2] = datos_arista # se guarda para ambos sentidos
        grafo[nodo2]["aristas"][nodo1] = datos_arista

# impresion de prueba
print(grafo[0])