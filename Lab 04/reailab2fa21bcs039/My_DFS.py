from My_Node import Node


def dfs(graph, initial_state, goal_state):
  frontier = [initial_state]
  explored = []
  while len(frontier) != 0:
    current_node = frontier.pop(len(frontier)-1)
    # print(current_node)
    explored.append(current_node)
    curren_children = 0
    for child in graph[current_node].actions:
      if child not in frontier and child not in explored:
        graph[child].parent = current_node
        if graph[child].state == goal_state:
          # print(explored)
          return action_sequence(graph, goal_state)
        curren_children += 1
        frontier.append(child)
    if curren_children==0:
      del explored[len(explored)-1]

def action_sequence(graph, goal_state):
  solution = [goal_state]
  current_parent = graph[goal_state].parent
  while current_parent is not None:
    solution.append(current_parent)
    current_parent = graph[current_parent].parent
  solution.reverse()
  return solution
