class Node:
    def __init__(this, state, parent, actions, total_cost):
        this.state = state
        this.parent = parent
        this.actions = actions
        this.total_cost = total_cost

    def __str__(this):
        print("State: ",this.state)
        print("Parent: ",this.parent)
        print("Actions: ",this.actions)
        print("Total Cost: ",this.total_cost)