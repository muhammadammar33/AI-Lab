import math


class Node:
    def __init__(self, state, parent, actions, heuristic, totalCost):
        self.state = state
        self.parent = parent
        self.actions = actions
        self.totalCost = totalCost
        self.heuristic = heuristic


def actionSequence(graph, initialState, goalState):
    solution = [goalState]
    currentParent = graph[goalState].parent
    while currentParent != None:
        solution.append(currentParent)
        currentParent = graph[currentParent].parent
    solution.reverse()
    return solution


def findMin(frontier):
    minV = math.inf
    node = ''
    for i in frontier:
        if minV > frontier[i][1]:
            minV = frontier[i][1]
            node = i
    return node


def Astar():
    initialState = 'A'
    goalState = 'O2'

    graph = {'A': Node('A', None, [('F', 1)], (0, 0), 0),
             'B': Node('B', None, [('C', 1), ('H', 1)], (2, 0), 0),
             'C': Node('C', None, [('B', 1), ('I', 1),  ('D', 1)], (3, 0), 0),
             'D': Node('D', None, [('C', 1), ('J', 1)], (4, 0), 0),
             'E': Node('E', None, [('M', 1)], 0, (8, 0)),
             'F': Node('F', None, [('A', 1), ('O', 1), ('G', 1)], (0, 1), 0),
             'G': Node('G', None, [('F', 1), ('H', 1), ('P', 1)], (1, 1), 0),
             'H': Node('H', None, [('G', 1), ('B', 1), ('I', 1), ('Q', 1)], (2, 1), 0),
             'I': Node('I', None, [('R', 1), ('J', 1), ('H', 1), ('C', 1)], (3, 1), 0),
             'J': Node('J', None, [('K', 1), ('S', 1), ('I', 1), ('D', 1)], (4, 1), 0),
             'K': Node('K', None, [('T', 1), ('J', 1)], (5, 1), 0),
             'L': Node('L', None, [('M', 1)], (7, 1), 0),
             'M': Node('M', None, [('E', 1), ('N', 1), ('L', 1)], (8, 1), 0),
             'N': Node('N', None, [('U', 1), ('M', 1)], (9, 1), 0),
             'O': Node('O', None, [('P', 1), ('V', 1), ('F', 1)], (0, 2), 0),
             'P': Node('P', None, [('O', 1), ('G', 1), ('W', 1), ('Q', 1)], (1, 2), 0),
             'Q': Node('Q', None, [('H', 1), ('P', 1), ('R', 1), ('X', 1)], (2, 2), 0),
             'R': Node('R', None, [('Q', 1), ('I', 1), ('Y', 1), ('S', 1)], (3, 2), 0),
             'S': Node('S', None, [('J', 1), ('R', 1), ('T', 1)], (4, 2), 0),
             'T': Node('T', None, [('S', 1), ('K', 1)], (5, 2), 0),
             'U': Node('U', None, [('N', 1)], (9, 2), 0),
             'V': Node('V', None, [('O', 1), ('W', 1)], (0, 3), 0),
             'W': Node('W', None, [('P', 1), ('X', 1), ('V', 1)], (1, 3), 0),
             'X': Node('X', None, [('W', 1), ('Q', 1), ('B1', 1), ('Y', 1)], (2, 3), 0),
             'Y': Node('Y', None, [('R', 1), ('X', 1)], (3, 3), 0),
             'Z': Node('Z', None, [('A1', 1), ('D1', 1)], (7, 3), 0),
             'A1': Node('A1', None, [('Z', 1)], (8, 3), 0),
             'B1': Node('B1', None, [('X', 1), ('H1', 1)], (2, 4), 0),
             'C1': Node('C1', None, [('L1', 1), ('D1', 1)], (6, 4), 0),
             'D1': Node('D1', None, [('C1', 1), ('Z', 1)], (7, 4), 0),
             'E1': Node('E1', None, [('M1', 1)], 0, (9, 4)),
             'F1': Node('F1', None, [('G1', 1)], (0, 5), 0),
             'G1': Node('G1', None, [('F1', 1), ('H1', 1)], (1, 5), 0),
             'H1': Node('H1', None, [('G1', 1), ('I1', 1), ('B1', 1), ('N1', 1)], (2, 5), 0),
             'I1': Node('I1', None, [('H1', 1), ('J1', 1), ('O1', 1)], (3, 5), 0),
             'J1': Node('J1', None, [('K1', 1), ('P1', 1), ('I1', 1)], (4, 5), 0),
             'K1': Node('K1', None, [('L1', 1), ('J1', 1)], (5, 5), 0),
             'L1': Node('L1', None, [('K1', 1), ('C1', 1)], (6, 5), 0),
             'M1': Node('M1', None, [('E1', 1), ('S1', 1)], (9, 5), 0),
             'N1': Node('N1', None, [('H1', 1), ('O1', 1)], (2, 6), 0),
             'O1': Node('O1', None, [('P1', 1), ('I1', 1), ('N1', 1)], (3, 6), 0),
             'P1': Node('P1', None, [('O1', 1), ('U1', 1), ('J1', 1)], (4, 6), 0),
             'Q1': Node('Q1', None, [('L1', 1), ('R1', 1)], (6, 6), 0),
             'R1': Node('R1', None, [('Q1', 1), ('W1', 1)], (7, 6), 0),
             'S1': Node('S1', None, [('Y1', 1), ('M1', 1)], (9, 6), 0),
             'T1': Node('T1', None, [('A2', 1)], (1, 7), 0),
             'U1': Node('U1', None, [('V1', 1), ('B2', 1), ('P1', 1)], (4, 7), 0),
             'V1': Node('V1', None, [('U1', 1), ('C2', 1)], (5, 7), 0),
             'W1': Node('W1', None, [('X1', 1), ('R1', 1)], (7, 7), 0),
             'X1': Node('X1', None, [('E2', 1), ('W1', 1), ('Y1', 1)], (8, 7), 0),
             'Y1': Node('Y1', None, [('S1', 1), ('F2', 1)], (9, 7), 0),
             'Z1': Node('Z1', None, [('A2', 1), ('G2', 1)], (0, 8), 0),
             'A2': Node('A2', None, [('Z1', 1), ('H2', 1), ('T1', 1)], (1, 8), 0),
             'B2': Node('B2', None, [('U1', 1), ('C2', 1), ('K2', 1)], (4, 8), 0),
             'C2': Node('C2', None, [('V1', 1), ('B2', 1), ('D2', 1)], (5, 8), 0),
             'D2': Node('D2', None, [('C2', 1), ('L2', 1)], (6, 8), 0),
             'E2': Node('E2', None, [('X1', 1), ('F2', 1), ('N2', 1)], (8, 8), 0),
             'F2': Node('F2', None, [('Y1', 1), ('O2', 1), ('E2', 1)], (9, 8), 0),
             'G2': Node('G2', None, [('Z1', 1), ('H2', 1)], (0, 9), 0),
             'H2': Node('H2', None, [('A2', 1), ('I2', 1)], (1, 9), 0),
             'I2': Node('I2', None, [('H2', 1), ('J2', 1)], (2, 9), 0),
             'J2': Node('J2', None, [('I2', 1), ('K2', 1)], (3, 9), 0),
             'K2': Node('K2', None, [('J2', 1), ('B2', 1)], (4, 9), 0),
             'L2': Node('L2', None, [('D2', 1), ('M2', 1)], (6, 9), 0),
             'M2': Node('M2', None, [('N2', 1), ('L2', 1)], (7, 9), 0),
             'N2': Node('N2', None, [('O2', 1), ('M2', 1), ('E2', 1)], (8, 9), 0),
             'O2': Node('O2', None, [('N2', 1), ('F2', 1)], (9, 9), 0)}

    frontier = dict()
    heuristicCost = math.sqrt(((graph[goalState].heuristic[0] - graph[initialState].heuristic[0])
                               ** 2) + ((graph[goalState].heuristic[1] - graph[initialState].heuristic[1]) ** 2))
    frontier[initialState] = (None, heuristicCost)
    explored = dict()
    while len(frontier) != 0:
        currentNode = findMin(frontier)
        print(currentNode)
        del frontier[currentNode]
        if graph[currentNode].state == goalState:
            return actionSequence(graph, initialState, goalState)

        heuristicCost = math.sqrt(((graph[goalState].heuristic[0] - graph[initialState].heuristic[0])
                                   ** 2) + ((graph[goalState].heuristic[1] - graph[initialState].heuristic[1]) ** 2))
        currentCost = graph[currentNode].totalCost
        explored[currentNode] = (
            graph[currentNode].parent, heuristicCost + currentCost)

        for child in graph[currentNode].actions:
            currentCost = child[1] + graph[currentNode].totalCost
            heuristicCost = math.sqrt(((graph[goalState].heuristic[0] - graph[initialState].heuristic[0])
                                       ** 2) + ((graph[goalState].heuristic[1] - graph[initialState].heuristic[1]) ** 2))

            if child[0] in explored:
                if graph[child[0]].parent == currentNode or child[0] == initialState or explored[child[0]][1] <= currentCost + heuristicCost:
                    continue

            if child[0] not in frontier:
                graph[child[0]].parent = currentNode
                graph[child[0]].totalCost = currentCost
                frontier[child[0]] = (
                    graph[child[0]].parent, currentCost + heuristicCost)

            else:
                if frontier[child[0]][1] < currentCost + heuristicCost:
                    graph[child[0]].parent = frontier[child[0]][0]
                    graph[child[0]].totalCost = frontier[child[0]][1] - \
                        heuristicCost

                else:
                    frontier[child[0]] = (
                        currentNode, currentCost + heuristicCost)
                    graph[child[0]].parent = frontier[child[0]][0]
                    graph[child[0]].totalCost = currentCost


solution = Astar()
print(solution)
