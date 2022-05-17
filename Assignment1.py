# input graph
g = {}
v = int(input("enter the num of vertices "))
start = input("enter start ")
g[start] = []

for i in range(v):
    current_key = list(g.keys())[i]
    print("Enter the connected nodes of " + current_key + "Press 0 for none")

    while (True):
        inp = input("--> ")
        if (inp == '0'):
            break
        g[current_key].append(inp)
        if (inp not in g.keys()):
            g[inp] = []

print(g)

# ---------------------------------------------
# BFS

print("BFS: ")

def bfs(visited, graph, node):
    visited.append(node)
    queue.append(node)
    while queue:
        s = queue.pop(0)
        print(s, end=" ")

        for neighbour in graph[s]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)


visited = [False] * v
graph = g
node = start
queue = []

bfs(visited, graph, node)

# DFS
print()
print("DFS: ")


def dfs(visited, graph, node):
    visited.append(node)
    stack.append(node)

    while stack:
        s = stack.pop()
        print(s, end=" ")

        for neighbour in graph[s]:
            if neighbour not in visited:
                visited.append(neighbour)
                stack.append(neighbour)


visited = [False] * v
graph = g
node = start
stack = []
dfs(visited, graph, node)

'''
enter the num of vertices 6
enter start a
Enter the connected nodes of aPress 0 for none
--> b
--> e
--> 0
Enter the connected nodes of bPress 0 for none
--> a
--> c
--> d
--> 0
Enter the connected nodes of ePress 0 for none
--> a
--> f
--> 0
Enter the connected nodes of cPress 0 for none
--> b
--> d
--> 0
Enter the connected nodes of dPress 0 for none
--> c
--> b
--> f
--> 0
Enter the connected nodes of fPress 0 for none
--> d
--> e
--> 0
{'a': ['b', 'e'], 'b': ['a', 'c', 'd'], 'e': ['a', 'f'], 'c': ['b', 'd'], 'd': ['c', 'b', 'f'], 'f': ['d', 'e']}
BFS:
a b e c d f
DFS:
a e f d c b
'''