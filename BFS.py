import ast
# Read the graph from a file
with open('graphBFS.txt') as file:
    data = file.read()
graph = ast.literal_eval(data)

visited = []  # List for visited nodes
queue = []   # Initialize a queue

# BFS function


def BFS(visited, graph, node):
    visited.append(node)
    queue.append(node)
    while queue:    # Creating loop to visit each node
        m = queue.pop(0)
        print(m, end=" ")
        for n in graph[m]:
            if n not in visited:
                visited.append(n)
                queue.append(n)


print("Following is the Breadth-First Search")
BFS(visited, graph, 'A')
