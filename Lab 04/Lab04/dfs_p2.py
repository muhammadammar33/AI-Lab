class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

def find_words(board, dictionary):
    def is_valid(x, y):
        return 0 <= x < len(board) and 0 <= y < len(board[0])

    def dfs(node, x, y, current_word):
        char = board[x][y]

        if char not in node.children:
            return

        current_word += char
        node = node.children[char]

        if node.is_end_of_word:
            found_words.add(current_word)

        visited[x][y] = True

        for dx, dy in directions:
            new_x, new_y = x + dx, y + dy
            if is_valid(new_x, new_y) and not visited[new_x][new_y]:
                dfs(node, new_x, new_y, current_word)

        visited[x][y] = False

    trie = Trie()
    for word in dictionary:
        trie.insert(word)

    directions = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1)]
    found_words = set()
    visited = [[False for _ in range(len(board[0]))] for _ in range(len(board))]

    for i in range(len(board)):
        for j in range(len(board[0])):
            dfs(trie.root, i, j, "")

    return list(found_words)

# Test case
board = [
    ['M', 'S', 'E', 'F'],
    ['R', 'A', 'T', 'D'],
    ['L', 'O', 'N', 'E'],
    ['K', 'A', 'F', 'B']
]
dictionary = ['START', 'NOTE', 'SAND', 'STONED']

result = find_words(board, dictionary)
print(result)  # Output: ['STONED', 'SAND', 'NOTE']
