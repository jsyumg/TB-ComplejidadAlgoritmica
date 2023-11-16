import heapq
import csv
import time
import ast
import networkx as nx
import random
import matplotlib.pyplot as plt
from tkinter import *
from tkinter import ttk
from tkinter import simpledialog
from tkinter import messagebox as mb
from tkinter import PhotoImage


# MST Algoritmo Prim
def prim(G):
    n = len(G)
    visited = [False] * n
    g = [float('inf')] * n
    mst = []
    min_peso = 0

    pq = []
    heapq.heappush(pq, (0, 0, -1))  # (g(s), s, parent)

    while pq:
        _, u, parent = heapq.heappop(pq)

        if not visited[u]:
            visited[u] = True

            if parent != -1:
                mst.append((parent, u, _))
                min_peso += _

            for v, w in G[u]:
                if not visited[v] and w < g[v]:
                    g[v] = w
                    heapq.heappush(pq, (w, v, u))

    return mst, min_peso


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
    min_peso = 0
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
            min_peso += w

    return mst, min_peso


# Visualizar el MST
def visualizar(mst):
    G = nx.Graph()

    for u, v, w in mst:
        G.add_edge(u, v, weight=w)

    pos = nx.spring_layout(G)
    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw(G, pos, with_labels=True, font_size=1, font_weight='normal', node_size=10)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels, font_size=3)

    plt.show()


class Aplicacion:
    def __init__(self):
        self.nodos = None
        self.grafo = None
        self.mst = None
        self.ventana = Tk()
        self.ventana.geometry("1024x576")
        self.ventana.resizable(False, False)
        self.ventana.title("Optimización de red de fibra óptica")
        self.ventana.config(background="#FFFFFF")
        self.configurar_componentes()

    def configurar_componentes(self):
        # codigo para centrar la ventana principal
        self.ventana.update_idletasks()
        ancho = self.ventana.winfo_width()
        alto = self.ventana.winfo_height()
        x = (self.ventana.winfo_screenwidth() // 2) - (ancho // 2)
        y = (self.ventana.winfo_screenheight() // 2) - (alto // 2)
        self.ventana.geometry(f"{ancho}x{alto}+{x}+{y}")

        # imagen background
        self.imagenbg = PhotoImage(file="imagenes/interfaz1.png")
        self.label_imagenbg = Label(self.ventana, image=self.imagenbg)
        self.label_imagenbg.place(x=0, y=0)
        self.label_imagenbg.pack()

        # creación de botones y entrys
        self.btnKruskal = Button(self.ventana, text="MST Algoritmo Kruskal", command=self.Kruskal, width="20", height="3")
        self.btnKruskal.place(x=100, y=300)
        self.btnPrim = Button(self.ventana, text="MST Algoritmo Prim", command=self.Prim, width="20", height="3")
        self.btnPrim.place(x=100, y=400)

    

    def construir_grafo(self, ruta_nodos, ruta_aristas):
        self.nodos = {} # datos de nodos
        with open(ruta_nodos, "r") as f:
            lector_csv = csv.DictReader(f)
            print("Leyendo archivo nodos.csv...")
            for fila in lector_csv:
                nodo_id = int(fila['Nodo'])
                datos_str = fila['Datos']
                datos_dict = ast.literal_eval(datos_str)
                self.nodos[nodo_id] = datos_dict


        self.grafo = {} # diccionario para almacenar grafo (lista de adyacencia)
        with open(ruta_aristas, "r") as file:
            read = csv.DictReader(file)
            print("Leyendo archivo aristas.csv...")
            for col in read:
                nodo1 = int(col["Nodo1"])
                nodo2 = int(col["Nodo2"])
                datos_arista = eval(col["Datos"])
                latencia = datos_arista['latencia']

                # crear lista de aristas para cada nuevo nodo
                if nodo1 not in self.grafo:
                    self.grafo[nodo1] = list()
                if nodo2 not in self.grafo:
                    self.grafo[nodo2] = list()
                
                # se guarda las aristas para ambos nodos al ser un grafo no digirido
                self.grafo[nodo1].append((nodo2, latencia))
                self.grafo[nodo2].append((nodo1, latencia))
        
        print("¡Lectura de datos completa!")
    
    def Kruskal(self):
        self.ventanaMST = Toplevel()
        self.ventanaMST.title("MST con Kruskal")
        self.ventanaMST.geometry("1024x576")
        self.ventanaMST.resizable(False, False)
        self.ventanaMST.config(background="#050A30")
        
        imagebg = PhotoImage(file="imagenes/interfaz2.png")
        label_imagebg = Label(self.ventanaMST, image=imagebg)
        label_imagebg.place(x=0, y=0)
        print("Hallando árbol de expansión mínima con Kruskal...")
        t_inicio = time.time()
        self.mst, min_peso = kruskal(self.grafo)
        t_fin = time.time()
        tiempo = t_fin - t_inicio
        self.labelMinPeso = Label(self.ventanaMST, text=f"La latencia mínima es: {min_peso}", font=("Arial", 14), fg="#FFFFFF", background="#050A30")
        self.labelMinPeso.place(x=550, y=200)
        self.labelTiempo = Label(self.ventanaMST, text=f"Tiempo de ejecución: {tiempo}", font=("Arial", 14), fg="#FFFFFF", background="#050A30")
        self.labelTiempo.place(x=550, y=250)
        btnVerMST = Button(self.ventanaMST, text="Ver árbol", command=self.ver_mst, width="20", height="3")
        btnVerMST.place(x=500, y=400)
        btnVerMST = Button(self.ventanaMST, text="Ver muestra de datos de arista", command=self.ver_muestra, width="25", height="3")
        btnVerMST.place(x=680, y=400)
        self.ventanaMST.mainloop()


    def Prim(self):
        self.ventanaMST = Toplevel()
        self.ventanaMST.title("MST con Prim")
        self.ventanaMST.geometry("1024x576")
        self.ventanaMST.resizable(False, False)
        self.ventanaMST.config(background="#050A30")
        
        imagebg = PhotoImage(file="imagenes/interfaz2.png")
        label_imagebg = Label(self.ventanaMST, image=imagebg)
        label_imagebg.place(x=0, y=0)
        print("Hallando árbol de expansión mínima con Prim...")
        t_inicio = time.time()
        self.mst, min_peso = prim(self.grafo)
        t_fin = time.time()
        tiempo = t_fin - t_inicio
        self.labelMinPeso = Label(self.ventanaMST, text=f"La latencia mínima es: {min_peso}", font=("Arial", 14), fg="#FFFFFF", background="#050A30")
        self.labelMinPeso.place(x=550, y=200)
        self.labelTiempo = Label(self.ventanaMST, text=f"Tiempo de ejecución: {tiempo}", font=("Arial", 14), fg="#FFFFFF", background="#050A30")
        self.labelTiempo.place(x=550, y=250)
        btnVerMST = Button(self.ventanaMST, text="Ver árbol", command=self.ver_mst, width="20", height="3")
        btnVerMST.place(x=500, y=400)
        btnVerMST = Button(self.ventanaMST, text="Ver muestra de datos de arista", command=self.ver_muestra, width="25", height="3")
        btnVerMST.place(x=680, y=400)
        self.ventanaMST.mainloop()
        
    
    def ver_mst(self):
        visualizar(self.mst)

    def ver_muestra(self):
        i = random.randint(0, 1000)
        u, v, w = self.mst[i]
        mb.showinfo("MUESTRA DE DATOS DE ARISTA DE MST", f"Se encontró la conexión entre: Switch modelo: {self.nodos[u]['Modelo']} y switch: {self.nodos[v]['Modelo']} con una latencia de {w} microsegundos")

    def ejecutar(self):
        mb.showinfo("LECTURA DE DATOS", "Al presionar aceptar, se empezará la lectura de datos para armar el grafo. Esto puede demorar unos segundos.")
        self.construir_grafo("datasets/nodos.csv", "datasets/aristas.csv")
        self.ventana.mainloop()

app = Aplicacion()
app.ejecutar()