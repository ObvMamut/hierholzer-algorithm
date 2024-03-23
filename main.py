def get_possible_nodes(current_node, edges):
    pos_nodes = []
    for edge in edges:
        if current_node in edge and edge[0] != current_node:
            pos_nodes.append(edge[0])
        elif current_node in edge and edge[1] != current_node:
            pos_nodes.append(edge[1])
    return pos_nodes


def hierholzer(path, edges):
    if len(edges) == 0:
        print(path)
        return True

    current_node = path[-1]
    pos_nodes = get_possible_nodes(current_node, edges)

    if pos_nodes == []:
        return False

    for next_node in pos_nodes:
        edge_to_remove = (current_node, next_node)
        if edge_to_remove in edges:
            edges.remove(edge_to_remove)
        else:
            edge_to_remove = (next_node, current_node)
            edges.remove(edge_to_remove)

        path.append(next_node)
        if hierholzer(path, edges):
            return True
        else:
            path.pop()
            edges.append(edge_to_remove)

    return False


path = [1] # Starting vertex  
edges = [(1,2), (1,3), (2,3), (2,3), (2,5), (3,4), (4,6), (4,6), (4,7), (5,6), (6,8), (7,9), (8,9), (8,9), (8,11), (9,10), (10,12), (10,12), (10,13), (11,12), (12,13)] # Example of undirected graph, in this case a graph created from the logo of the Olympic Games
hierholzer(path, edges)

# -- ObvMamut

