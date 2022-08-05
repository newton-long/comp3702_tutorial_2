
from PuzzleNode import Node
from breadth_first_search import breadth_first_search

if __name__ == '__main__':
    init_state = Node([
        "7", "2", "4",
        "5", "3", "6",
        "8", "_", "1"], None, None)
    goal_state = Node([
        "1", "2", "3",
        "4", "5", "6",
        "7", "8", "_"], None, None)

    breadth_first_search(init_state, goal_state)
