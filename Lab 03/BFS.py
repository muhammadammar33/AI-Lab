class Node:
    def __init__(self, state, parent, actions, totalCost):
        self.state = state
        self.parent = parent
        self.actions = actions
        self.totalCost = totalCost


def BFS():
    initialState = 'Arad'
    goalState = 'Bucharset'

    graph = {'Neamt': Node('Neamt', None, ['Iasi'], [87]),
             'Iasi': Node('Iasi', None, ['Vaslui'], [92]),
             'Vaslui': Node('Vaslui', None, ['Urziceni'], [142]),
             'Urziceni': Node('Urziceni', None, ['Hirsowa', 'Bucharset'], [98, 85]),
             'Hirsowa': Node('Hirsowa', None, ['Eforte', 'Urziceni'], [86, 98]),
             'Eforte': Node('Eforte', None, ['Hirsowa'], [86]),
             'Bucharset': Node('Bucharset', None, ['Urziceni', 'Guirgiu', 'Fagaras', 'Pitesti'], [85, 90, 211, 101]),
             'Guirgiu': Node('Guirgiu', None, ['Bucharset'], [90]),
             'Fagaras': Node('Fagaras', None, ['Bucharset', 'Sibiu'], [211, 99]),
             'Pitesti': Node('Pitesti', None, ['Bucharset', 'Rimnicu Vilcea'], [101, 97]),
             'Rimnicu Vilcea': Node('Rimnicu Vilcea', None, ['Pitesti', 'Craiova', 'Sibiu'], [97, 80, 146]),
             'Oradea': Node('Oradea', None, ['Zerind', 'Sibiu'], [71, 151]),
             'Zerind': Node('Zerind', None, ['Arad', 'Oradea'], [75, 71]),
             'Arad': Node('Arad', None, ['Zerind', 'Sibiu', 'TimiSoara'], [75, 140, 118]),
             'TimiSoara': Node('TimiSoara', None, ['Arad', 'Lugoj'], [118, 111]),
             'Lugoj': Node('Lugoj', None, ['TimiSoara', 'Mehadia'], [111, 70]),
             'Mehadia': Node('Mehadia', None, ['Lugoj', 'Drobeta'], [70, 75]),
             'Drobeta': Node('Drobeta', None, ['Mehadia', 'Craiova'], [75, 120]),
             'Craiova': Node('Craiova', None, ['Drobeta', 'Pitesi', 'Rimnicu Vilcea'], [120, 138, 146]),
             'Sibiu': Node('Sibiu', None, ['Oradea', 'Arad', 'Fagaras', 'Rimnicu Vilcea'], [151, 140, 99, 80])
             }
    frontier = [initialState]
    explored = []
    # frontier.append(start)
    while len(frontier) != 0:
        current_node = frontier.pop(0)
        explored.append(current_node)

        for child in graph[current_node].actions:
            if child not in frontier and child not in explored:
                graph[child].parent = current_node
                if graph[child].state == goalState:
                    return actionSequence(graph, initialState, goalState)
                frontier.append(child)


def actionSequence(graph, initialState, goalState):
    solution = [goalState]
    currentparent = graph[goalState].parent
    while currentparent != None:
        solution.append(currentparent)
        currentparent = graph[currentparent].parent
    solution.reverse()
    return solution


solution = BFS()
print(solution)
