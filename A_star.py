import ast
# Read the graph from a file
with open('graphA_Star.txt') as file1:
    data1 = file1.read()
graph = ast.literal_eval(data1)


# Read the H_table from a file
with open('tableA_Star.txt') as file2:
    data2 = file2.read()
table = ast.literal_eval(data2)


# Function fot Calculating The Total_Cost Of The Path
def path_f_cost(path):
    g_cost = 0
    for (node, cost) in path:
        g_cost += cost
    lastnode = path[-1][0]
    h_cost = table[lastnode]
    f_cost = g_cost + h_cost
    return f_cost, lastnode

# A_Star function


def A_star_search(graph, start, goal):
    visited = []            # List for visited nodes
    queue = [[(start, 0)]]  # Initialize a queue
    while queue:            # Creating loop to visit each node
        # Sorting The Queue (key=total cost for the path)
        queue.sort(key=path_f_cost)
        path = queue.pop(0)
        node = path[-1][0]
        if node in visited:
            continue
        visited.append(node)
        if node == goal:
            return path
        else:
            adj_nodes = graph.get(node, [])
            for (node2, cost) in adj_nodes:
                new_path = path.copy()
                new_path.append((node2, cost))
                queue.append(new_path)


# Driver Code
solution = A_star_search(graph, 'A', 'J')
print("The solution is", solution)
print("Cost of solution is", path_f_cost(solution)[0])
