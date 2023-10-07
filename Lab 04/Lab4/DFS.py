
def DFS(final,visited,stack,graph):
    # print(stack)
    current=stack.pop(len(stack)-1)
    visited.append(current)
    # print(current)
    if current==final:
        return
    # if len(stack)==0:
    #     return
    for child in graph[current].actions:
        if child not in visited and child not in stack:
            stack.append(child)
    DFS(final,visited,stack,graph)