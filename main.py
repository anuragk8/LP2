from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
        self.vertices = []

    def addEdge(self, u, v):
        self.graph[u].append(v)
        if u in self.vertices:
            pass
        else:
            self.vertices.append(u)

        print(u , "=>" , v)

    def DFS(self, v):
        visited = set()
        self.DFSvisited(v, visited)

    def DFSvisited(self, v, visited):
        visited.add(v)
        print(v, end = ' ')

        for neighbour in self.graph[v]:
            if neighbour not in visited:
                self.DFSvisited(neighbour, visited)


    def BFS(self, s):

        visited = [False] * (max(self.graph) + 1)

        queue = []

        queue.append(s)
        visited[s] = True

        while queue:
            s = queue.pop(0)
            print(s, end=" ")

            for i in self.graph[s]:
                if visited[i] == False:
                    queue.append(i)
                    visited[i] = True

    def Search(self):
        s_vertex = int(input("Enter the vertex you would like to search for: "))
        if s_vertex in self.vertices:
            print(s_vertex, "is present in the graph")
        else:
            print(s_vertex, "Not Found")



g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)



choice = int(input("1.Perform DFS 2.Perform BFS 3.Search: "))

if choice == 1:
    vertex = int(input("Enter Vertex you want to traverse from: "))
    print("DFS:", end="\n")
    g.DFS(vertex)
elif choice == 2:
    vertex = int(input("Enter Vertex you want to traverse from: "))
    print("BFS:", end="\n")
    g.BFS(vertex)
else:
    g.Search()


#print("DFS traversal of graph from vertex", vertex)





