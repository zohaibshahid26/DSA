import customtkinter as ctk
import networkx as nx
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from collections import defaultdict, deque


class GraphUsingList:
    def __init__(self):
        self.adj_list = defaultdict(list)
        self.start_vertex = None

    def add_vertex(self, vertex):
        if vertex not in self.adj_list:
            self.adj_list[vertex] = []
            if self.start_vertex is None:
                self.start_vertex = vertex

    def remove_vertex(self, vertex):
        if vertex in self.adj_list:
            del self.adj_list[vertex]
            for adj_vertex in self.adj_list:
                self.adj_list[adj_vertex] = [v for v in self.adj_list[adj_vertex] if v != vertex]

    def add_edge(self, start_vertex, end_vertex):
        if start_vertex in self.adj_list and end_vertex in self.adj_list:
            self.adj_list[start_vertex].append(end_vertex)

    def remove_edge(self, start_vertex, end_vertex):
        if start_vertex in self.adj_list and end_vertex in self.adj_list:
            self.adj_list[start_vertex] = [v for v in self.adj_list[start_vertex] if v != end_vertex]

    def dfs(self):
        visited = []
        stack = deque()

        for start_vertex in self.adj_list.keys():
            if start_vertex not in visited:
                stack.append(start_vertex)

                while stack:
                    vertex = stack.pop()

                    if vertex not in visited:
                        visited.append(vertex)

                    for neighbor in self.adj_list[vertex]:
                        if neighbor not in visited:
                            stack.append(neighbor)

        return visited

    def bfs(self):
        visited = []
        queue = deque()

        # Perform BFS for each component in the graph
        for start_vertex in self.adj_list.keys():
            if start_vertex not in visited:
                queue.append(start_vertex)
                visited.append(start_vertex)

                while queue:
                    vertex = queue.popleft()

                    for neighbor in self.adj_list[vertex]:
                        if neighbor not in visited:
                            queue.append(neighbor)
                            visited.append(neighbor)

        return visited

    def show_graph(self):
        G = nx.DiGraph()

        for vertex, neighbors in self.adj_list.items():
            G.add_node(vertex)
            for neighbor in neighbors:
                G.add_edge(vertex, neighbor)

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

graph = GraphUsingList()


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
        output_text.insert(ctk.END, result)
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
        output_text.insert(ctk.END, result)

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
