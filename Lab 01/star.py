print("Enter size")
size = int(input())


def star(size):
    # Upper part of the Star of David
    for i in range(size // 4):
        spaces = " " * (size // 4 - i + size // 4)
        stars = "*" * (2 * i + 1)
        print(spaces + stars + spaces)

    # Middle line of the Star of David
    for i in range(size//4-1, 0, -1):
        for j in range(size//4-i-1):
            print(" ", end="")
        for j in range(2*i+size-size//4-2):
            print("*", end="")
        print()

    for i in range(size//4):
        for j in range(size//4-i-1):
            print(" ", end="")
        for j in range(2*i+size-size//4-2):
            print("*", end="")
        print()

    # Lower part of the Star of David
    for i in reversed(range(size // 4)):
        spaces = " " * (size // 4 - i + size // 4)
        stars = "*" * (2 * i + 1)
        print(spaces + stars + spaces)


star(size)
