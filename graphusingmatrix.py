import customtkinter as ctk
import networkx as nx
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from collections import deque


class GraphUsingMatrix:
    def __init__(self):
        self.vertices = []
        self.adj_matrix = []
        self.start_vertex = None

    def add_vertex(self, vertex):
        if vertex not in self.vertices:
            self.vertices.append(vertex)
            for row in self.adj_matrix:
                row.append(0)
            self.adj_matrix.append([0] * len(self.vertices))

            if not self.start_vertex:
                self.start_vertex = vertex

    def remove_vertex(self, vertex):
        if vertex in self.vertices:
            index = self.vertices.index(vertex)
            self.vertices.pop(index)
            self.adj_matrix.pop(index)
            for row in self.adj_matrix:
                row.pop(index)

    def add_edge(self, start_vertex, end_vertex):
        if start_vertex in self.vertices and end_vertex in self.vertices:
            start_index = self.vertices.index(start_vertex)
            end_index = self.vertices.index(end_vertex)
            self.adj_matrix[start_index][end_index] = 1

    def remove_edge(self, start_vertex, end_vertex):
        if start_vertex in self.vertices and end_vertex in self.vertices:
            start_index = self.vertices.index(start_vertex)
            end_index = self.vertices.index(end_vertex)
            self.adj_matrix[start_index][end_index] = 0

        def bfs(self):
        if not self.vertices:
            return []

        visited = []
        queue = deque()
        remaining_vertices = set(self.vertices)

        while remaining_vertices:
            start_vertex = remaining_vertices.pop()
            visited.append(start_vertex)
            queue.append(start_vertex)

            while queue:
                vertex = queue.popleft()
                vertex_index = self.vertices.index(vertex)
                neighbors = [self.vertices[i] for i in range(len(self.vertices)) if self.adj_matrix[vertex_index][i] == 1]

                for neighbor in neighbors:
                    if neighbor not in visited:
                        visited.append(neighbor)
                        queue.append(neighbor)
                        remaining_vertices.discard(neighbor)

        return visited


    def dfs(self):
        if not self.vertices:
            return []

        visited = []
        stack = deque()
        remaining_vertices = set(self.vertices)

        while remaining_vertices:
            start_vertex = remaining_vertices.pop()
            visited.append(start_vertex)
            stack.append(start_vertex)

            while stack:
                vertex = stack.pop()
                vertex_index = self.vertices.index(vertex)
                neighbors = [self.vertices[i] for i in range(len(self.vertices)) if self.adj_matrix[vertex_index][i] == 1]

                for neighbor in neighbors:
                    if neighbor not in visited:
                        visited.append(neighbor)
                        stack.append(neighbor)
                        remaining_vertices.discard(neighbor)

        return visited

    def show_graph(self):

        G = nx.DiGraph()

        for vertex in self.vertices:
            G.add_node(vertex)

        for i in range(len(self.vertices)):
            for j in range(len(self.vertices)):
                if self.adj_matrix[i][j] == 1:
                    G.add_edge(self.vertices[i], self.vertices[j])

        fig = Figure(figsize=(5, 4), dpi=100)
        ax = fig.add_subplot(111)

        pos = nx.spring_layout(G, seed=42)
        nx.draw(G, pos, with_labels=True, arrows=True, ax=ax)

        root = ctk.CTk()
        root.title("Graph")
        canvas = FigureCanvasTkAgg(fig, master=root)
        canvas.draw()
        canvas.get_tk_widget().pack()

        root.mainloop()


root = ctk.CTk()
root.iconbitmap()
root.geometry('300x330')
root.title("Graph")

graph = GraphUsingMatrix()


def add_vertex_button():
    def add_vertex():
        vertex = entry.get()
        graph.add_vertex(vertex.upper())
        newRoot.destroy()

    newRoot = ctk.CTkToplevel()
    newRoot.title("Add Vertex")
    newRoot.geometry('250x150')
    newRoot.iconbitmap()

    entry = ctk.CTkEntry(master=newRoot, text_color='white')
    button = ctk.CTkButton(master=newRoot, text="Add", command=add_vertex, width=15)
    entry.pack(pady=30)
    button.pack()
    newRoot.mainloop()


def remove_vertex_button():
    def remove_vertex():
        vertex = entry.get()
        graph.remove_vertex(vertex)
        newRoot.destroy()

    newRoot = ctk.CTkToplevel()
    newRoot.title("Remove Vertex")
    newRoot.geometry('250x150')
    newRoot.iconbitmap()

    entry = ctk.CTkEntry(master=newRoot, text_color='white')
    button = ctk.CTkButton(master=newRoot, text="Remove", command=remove_vertex, width=15)
    entry.pack(pady=30)
    button.pack()
    newRoot.mainloop()


def add_edge_button():
    def add_edge():
        source = entry1.get()
        destination = entry2.get()
        graph.add_edge(source, destination)
        newRoot.destroy()

    newRoot = ctk.CTkToplevel()
    newRoot.title("Add Edge")
    newRoot.geometry('250x150')
    newRoot.iconbitmap()

    entry1 = ctk.CTkEntry(master=newRoot, text_color='white', placeholder_text="Source Vertex")
    entry2 = ctk.CTkEntry(master=newRoot, text_color='white', placeholder_text="Destination Vertex")
    button = ctk.CTkButton(master=newRoot, text="Add", command=add_edge, width=15)
    entry1.pack(pady=10)
    entry2.pack(pady=10)
    button.pack()
    newRoot.mainloop()


def remove_edge_button():
    def remove_edge():
        source = entry1.get()
        destination = entry2.get()
        graph.remove_edge(source, destination)
        newRoot.destroy()

    newRoot = ctk.CTkToplevel()
    newRoot.title("Remove Edge")
    newRoot.geometry('250x150')
    newRoot.iconbitmap()

    entry1 = ctk.CTkEntry(master=newRoot, text_color='white', placeholder_text="Source Vertex")
    entry2 = ctk.CTkEntry(master=newRoot, text_color='white', placeholder_text="Destination Vertex")
    button = ctk.CTkButton(master=newRoot, text="Remove", command=remove_edge, width=15)
    entry1.pack(pady=10)
    entry2.pack(pady=10)
    button.pack()
    newRoot.mainloop()


def bfs_button():
    def bfs_traversal():
        result = graph.bfs()
        print(result)
        output_text.insert(ctk.END, str(result))
        output_text.insert(ctk.END, "\n")

    bfsRoot = ctk.CTkToplevel()
    bfsRoot.title("BFS Traversal")
    bfsRoot.geometry('250x150')

    output_text = ctk.CTkTextbox(master=bfsRoot, width=400, height=10)
    output_text.pack(pady=20)

    button = ctk.CTkButton(master=bfsRoot, text="Run BFS", command=bfs_traversal, width=15)
    button.pack()

    bfsRoot.mainloop()


def dfs_button():
    def dfs_traversal():
        result = graph.dfs()
        output_text.insert(ctk.END, str(result))

    dfsRoot = ctk.CTkToplevel()
    dfsRoot.title("DFS Traversal")
    dfsRoot.geometry('250x150')

    button = ctk.CTkButton(master=dfsRoot, text="Run DFS", command=dfs_traversal, width=15)
    output_text = ctk.CTkTextbox(master=dfsRoot, text_color='white', width=400, height=10)
    output_text.pack(pady=20)
    button.pack()

    dfsRoot.mainloop()


frame = ctk.CTkFrame(master=root)
frame.pack(pady=15)
ctk.CTkButton(master=frame, text="Add a vertex", command=add_vertex_button).pack(pady=5)
ctk.CTkButton(master=frame, text="Add a an edge", command=add_edge_button).pack(pady=5)
ctk.CTkButton(master=frame, text="Remove an Edge", command=remove_edge_button).pack(pady=5)
ctk.CTkButton(master=frame, text="Remove a vertex", command=remove_vertex_button).pack(pady=5)
ctk.CTkButton(master=frame, text="BFS", command=bfs_button).pack(pady=5)
ctk.CTkButton(master=frame, text="DFS", command=dfs_button).pack(pady=5)
ctk.CTkButton(master=frame, text="Show Graph", command=graph.show_graph).pack(pady=5)
ctk.CTkButton(master=frame, text="Quit", command=root.quit).pack(pady=5)

root.mainloop()
