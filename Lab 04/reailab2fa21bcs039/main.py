from My_DFS import dfs
from My_Node import Node

graph = {
    'A': Node(state='A', parent=None, actions=['B', 'C', 'E'],
              total_cost=None),
    'B': Node(state='B', parent=None, actions=['A', 'D', 'E'],
              total_cost=None),
    'C': Node(state='C', parent=None, actions=['B', 'F', 'G'],
              total_cost=None),
    'D': Node(state='D', parent=None, actions=['B', 'E'], total_cost=None),
    'E': Node(state='E', parent=None, actions=['B', 'A', 'D'],
              total_cost=None),
    'F': Node(state='F', parent=None, actions=['C'], total_cost=None),
    'G': Node(state='G', parent=None, actions=['C'], total_cost=None)
}

# print(bfs(graph=graph, initial_state='A', goal_state='F'))


def problem_1():
  graph = {
      'Oradea':
      Node(state='Oradea',
           parent=None,
           actions=['Zerind', 'Sibiu'],
           total_cost=[71, 151]),
      'Zerind':
      Node(state='Zerind',
           parent=None,
           actions=['Arad', 'Oradea'],
           total_cost=[75, 71]),
      'Arad':
      Node(state='Arad',
           parent=None,
           actions=['Zerind', 'Sibiu', 'Timisoara'],
           total_cost=[75, 140, 118]),
      'Sibiu':
      Node(state='Sibiu',
           parent=None,
           actions=['Oradea', 'Arad', 'Fagaras', 'Rimnicu Vilcea'],
           total_cost=[151, 140, 99, 80]),
      'Timisoara':
      Node(state='Timisoara',
           parent=None,
           actions=['Arad', 'Lugoj'],
           total_cost=[]),
      'Lugoj':
      Node(state='Lugoj',
           parent=None,
           actions=['Timisoara', 'Mehadia'],
           total_cost=[]),
      'Mehadia':
      Node(state='Mehadia',
           parent=None,
           actions=['Lugoj', 'Drobeta'],
           total_cost=[]),
      'Drobeta':
      Node(state='Drobeta',
           parent=None,
           actions=['Mehadia', 'Craiova'],
           total_cost=[]),
      'Craiova':
      Node(state='Craiova',
           parent=None,
           actions=['Drobeta', 'Rimnicu Vilcea', 'Pitesti'],
           total_cost=[]),
      'Rimnicu Vilcea':
      Node(state='Rimnicu Vilcea',
           parent=None,
           actions=['Craiova', 'Sibiu', 'Pitesti'],
           total_cost=[]),
      'Pitesti':
      Node(state='Pitesti',
           parent=None,
           actions=['Rimnicu Vilcea', 'Craiova', 'Bucharest'],
           total_cost=[]),
      'Fagaras':
      Node(state='Fagaras',
           parent=None,
           actions=['Sibiu', 'Bucharest'],
           total_cost=[]),
      'Bucharest':
      Node(state='Bucharest',
           parent=None,
           actions=['Fagaras', 'Pitesti', 'Giurgiu', 'Urzieeni'],
           total_cost=[]),
      'Giurgiu':
      Node(state='Giurgiu', parent=None, actions=['Bucharest'], total_cost=[]),
      'Urzieeni':
      Node(state='Urzieeni',
           parent=None,
           actions=['Bucharest', 'Hirsova', 'Vaslui'],
           total_cost=[]),
      'Hirsova':
      Node(state='Hirsova',
           parent=None,
           actions=['Urzieeni', 'Eforie'],
           total_cost=[]),
      'Eforie':
      Node(state='Eforie', parent=None, actions=['Hirsova'], total_cost=[]),
      'Vaslui':
      Node(state='Vaslui',
           parent=None,
           actions=['Urzieeni', 'Iasi'],
           total_cost=[]),
      'Iasi':
      Node(state='Iasi',
           parent=None,
           actions=['Vaslui', 'Neamt'],
           total_cost=[]),
      'Neamt':
      Node(state='Neamt', parent=None, actions=['Isai'], total_cost=[])
  }

  print(dfs(graph=graph, initial_state='Arad', goal_state='Bucharest'))


problem_1()


def problem_2():
  graph = {
    'M' : Node('M',None, ['R', 'A', 'S'], None),
    '' : Node('', None, [], None),
    '' : Node('', None, [], None),
    '' : Node('', None, [], None),
    '' : Node('', None, [], None),
    '' : Node('', None, [], None),
    '' : Node('', None, [], None),
    '' : Node('', None, [], None),
    '' : Node('', None, [], None),
    '' : Node('', None, [], None),
    '' : Node('', None, [], None),
    '' : Node('', None, [], None),
    '' : Node('', None, [], None),
    '' : Node('', None, [], None),
    '' : Node('', None, [], None),
    '' : Node('', None, [], None),
  }