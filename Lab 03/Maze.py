from collections import deque

# Define the maze as a 2D grid
maze = [
    ["W", "W", "W", "W", "W", "E", "W", "W"],
    ["W", " ", " ", " ", " ", " ", " ", "W"],
    ["W", " ", "W", "W", "W", "W", " ", "W"],
    ["W", " ", "W", "S", "W", " ", " ", "W"],
    ["W", " ", "W", " ", "W", "W", " ", "W"],
    ["W", " ", "W", " ", "W", " ", " ", "W"],
    ["W", " ", " ", " ", " ", " ", " ", "W"],
    ["W", "W", "W", "W", "W", "W", "W", "W"],
]

# Define possible moves (up, down, left, right)
moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]
move_names = ["right", "left", "down", "up"]


def is_valid(x, y):
    return 0 <= x < len(maze) and 0 <= y < len(maze) and maze[x][y] != "W"


def bfs(maze, start):
    queue = deque([(start, [])])
    visited = set()

    while queue:
        (x, y), path = queue.popleft()
        visited.add((x, y))

        for (dx, dy), move_name in zip(moves, move_names):
            new_x, new_y = x + dx, y + dy
            if (new_x, new_y) not in visited and is_valid(new_x, new_y):
                if maze[new_x][new_y] == "E":
                    return path + [move_name]
                else:
                    queue.append(((new_x, new_y), path + [move_name]))

    return None

start = None
for i in range(len(maze)):
    for j in range(len(maze[0])):
        if maze[i][j] == "S":
            start = (i, j)
            break

if start is not None:
    path = bfs(maze, start)
    if path:
        print("Path to the exit:", " -> ".join(path))
        print(start)
    else:
        print("No path to the exit found.")
else:
    print("Starting position 'S' not found in the maze.")
