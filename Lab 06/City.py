import math


class Node:
    def __init__(self, state, parent, actions, totalCost):
        self.state = state
        self.parent = parent
        self.actions = actions
        self.totalCost = totalCost


def findMin(frontier):
    minV = math.inf
    node = ''
    for i in frontier:
        if minV > frontier[i][1]:
            minV = frontier[i][1]
            node = i
    return node


def actionSequence(graph, initialState, goalState):
    solution = [goalState]
    currentParent = graph[goalState].parent
    while currentParent != None:
        solution.append(currentParent)
        currentParent = graph[currentParent].parent
    solution.reverse()
    return solution


def UCS():
    initialState = 'Neamt'
    goalState = 'Arad'

    graph = {'Neamt': Node('Neamt', None, [('Iasi', 87)], 0),
             'Iasi': Node('Iasi', None, [('Neamt', 87), ('Vaslui', 92)], 0),
             'Vaslui': Node('Vaslui', None, [('Iasi', 92), ('Urziceni', 142)], 0),
             'Urziceni': Node('Urziceni', None, [('Vaslui', 142), ('Bucharset', 85), ('Hirsowa', 98)], 0),
             'Hirsowa': Node('Hirsowa', None, [('Eforte', 86), ('Urziceni', 98)], 0),
             'Eforte': Node('Eforte', None, [('Hirsowa', 86)], 0),
             'Bucharset': Node('Bucharset', None, [('Urziceni', 85), ('Guirgiu', 90), ('Fagaras', 211), ('Pitesti', 101)], 0),
             'Guirgiu': Node('Guirgiu', None, [('Bucharset', 90)], 0),
             'Fagaras': Node('Fagaras', None, [('Bucharset', 211), ('Sibiu', 99)], 0),
             'Pitesti': Node('Pitesti', None, [('Bucharset', 101), ('Rimnicu Vilcea', 97), ('Craiova', 138)], 0),
             'Rimnicu Vilcea': Node('Rimnicu Vilcea', None, [('Pitesti', 97), ('Craiova', 146), ('Sibiu', 80)], 0),
             'Oradea': Node('Oradea', None, [('Zerind', 71), ('Sibiu', 151)], 0),
             'Zerind': Node('Zerind', None, [('Arad', 75), ('Oradea', 71)], 0),
             'Arad': Node('Arad', None, [('Zerind', 75), ('Sibiu', 140), ('TimiSoara', 118)], 0),
             'TimiSoara': Node('TimiSoara', None, [('Arad', 118), ('Lugoj', 111)], 0),
             'Lugoj': Node('Lugoj', None, [('TimiSoara', 111), ('Mehadia', 70)], 0),
             'Mehadia': Node('Mehadia', None, [('Lugoj', 70), ('Drobeta', 75)], 0),
             'Drobeta': Node('Drobeta', None, [('Mehadia', 75), ('Craiova', 120)], 0),
             'Craiova': Node('Craiova', None, [('Drobeta', 120), ('Pitesti', 138), ('Rimnicu Vilcea', 146)], 0),
             'Sibiu': Node('Sibiu', None, [('Oradea', 151), ('Arad', 140), ('Fagaras', 99), ('Rimnicu Vilcea', 80)], 0),
             }

    frontier = dict()
    frontier[initialState] = (None, 0)
    explored = []
    while len(frontier) != 0:
        currentNode = findMin(frontier)
        del frontier[currentNode]
        if graph[currentNode].state not in explored:
            explored.append(graph[currentNode].state)
            if graph[currentNode].state == goalState:
                path = actionSequence(graph, initialState, goalState)
                cost = graph[goalState].totalCost
                return path, cost

            explored.append(currentNode)
            for child in graph[currentNode].actions:
                currentCost = child[1] + graph[currentNode].totalCost
                if child[0] not in frontier and child[0] not in explored:
                    graph[child[0]].parent = currentNode
                    graph[child[0]].totalCost = currentCost
                    frontier[child[0]] = (
                        graph[child[0]].parent, graph[child[0]].totalCost)
                elif child[0] in frontier:
                    if frontier[child[0]][1] < currentCost:
                        graph[child[0]].parent = frontier[child[0]][0]
                        graph[child[0]].totalCost = frontier[child[0]][1]
                    else:
                        frontier[child[0]] = (currentNode, currentCost)
                        graph[child[0]].parent = frontier[child[0]][0]
                        graph[child[0]].totalCost = frontier[child[0]][1]


solution = UCS()
print(solution)
