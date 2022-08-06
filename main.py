
from PuzzleNode import Node
from breadth_first_search import breadth_first_search, breadth_first_search_original
from depth_first_search import depth_first_search, depth_first_search_original

if __name__ == '__main__':
    # init_state = Node(["7", "2", "4", "5", "3", "6", "8", "_", "1"], None, None)
    # goal_state = Node(["1", "2", "3", "4", "5", "6", "7", "8", "_"], None, None)
    #
    # depth_first_search_original(init_state, goal_state)

    # init_state = [
    #     [7, 2, 4],
    #     [5, 3, 6],
    #     [8, -1, 1]
    # ]
    # goal_state = [
    #     [1, 2, 3],
    #     [4, 5, 6],
    #     [7, 8, -1]
    # ]
    # steps = depth_first_search(init_state, goal_state)

    init_state = [
        [9, 2, 1, 4],
        [6, 13, 8, 14],
        [11, 5, 3, -1],
        [10, 12, 7, 15]
    ]
    goal_state = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, -1]
    ]
    depth_first_search(init_state, goal_state)