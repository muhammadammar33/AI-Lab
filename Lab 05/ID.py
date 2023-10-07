graph = {
    'Arad': {'Sibiu': 140, 'Zerind': 75, 'Timisoara': 118},
    'Zerind': {'Arad': 75, 'Oradea': 71},
    'Oradea': {'Zerind': 71, 'Sibiu': 151},
    'Sibiu': {'Rimnicu Vilcea': 80, 'Arad': 140, 'Oradea': 151, 'Fagaras': 99},
    'Fagaras': {'Sibiu': 99, 'Bucharest': 211},
    'Rimnicu Vilcea': {'Pitesti': 97, 'Sibiu': 80, 'Craiova': 146},
    'Timisoara': {'Arad': 118, 'Lugoj': 111},
    'Lugoj': {'Timisoara': 111, 'Mehadia': 70},
    'Mehadia': {'Lugoj': 70, 'Drobeta': 75},
    'Drobeta': {'Mehadia': 75, 'Craiova': 120},
    'Craiova': {'Drobeta': 120, 'Rimnicu Vilcea': 146, 'Pitesti': 138},
    'Pitesti': {'Craiova': 138, 'Rimnicu Vilcea': 97, 'Bucharest': 101},
    'Bucharest': {'Fagaras': 211, 'Pitesti': 101, 'Giurgiu': 90}
}


def iterative_deepening_search(start, goal, max_depth):
    for depth in range(max_depth + 1):
        visited = set()
        path = []
        if depth_limited_search(start, goal, depth, visited, path):
            return path
    return None


def depth_limited_search(node, goal, depth, visited, path):
    if depth == 0:
        return False
    if node == goal:
        path.append(node)
        return True
    visited.add(node)
    for neighbor, cost in graph[node].items():
        if neighbor not in visited:
            if depth_limited_search(neighbor, goal, depth - 1, visited, path):
                path.append(node)
                return True
    return False


# Find the shortest path from Arad to Bucharest with IDS (maximum depth = 10)
start_city = 'Arad'
goal_city = 'Bucharest'
max_depth = 10

result = iterative_deepening_search(start_city, goal_city, max_depth)

if result:
    result.reverse()
    print("Shortest path from {} to {}:".format(start_city, goal_city))
    print(" -> ".join(result))
else:
    print("No path found from {} to {} within the given depth.".format(
        start_city, goal_city))
