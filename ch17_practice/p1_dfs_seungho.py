firstp_graph = {
    1:[2,3,4],
    2:[1,5],
    3:[1,6],
    4:[1,6],
    5:[2,6],
    6:[3,4,5]
}

def p1_dfs(graph, start_node):
    stack = []
    visited = []
    stack.append(start_node)
    
    while stack:
        node = stack.pop()
        if node not in visited:
            stack.extend(reversed(graph[node]))
            visited.append(node)
    return visited

print("dfs - ", end='')
print(p1_dfs(firstp_graph,1))
            