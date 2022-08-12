
from breadth_first_search import breadth_first_search
from depth_first_search import depth_first_search

if __name__ == '__main__':
    init_state = (
        (7, 2, 4),
        (5, 3, 6),
        (8, -1, 1)
    )
    goal_state = (
        (1, 2, 3),
        (4, 5, 6),
        (7, 8, -1)
    )
    steps = breadth_first_search(init_state, goal_state)
    steps = depth_first_search(init_state, goal_state)

    # this will use over 60GB of memory...
    # see Tutorial 3 for solution to 15-puzzle
    # init_state = (
    #     (9, 2, 1, 4),
    #     (6, 13, 8, 14),
    #     (11, 5, 3, -1),
    #     (10, 12, 7, 15)
    # )
    # goal_state = (
    #     (1, 2, 3, 4),
    #     (5, 6, 7, 8),
    #     (9, 10, 11, 12),
    #     (13, 14, 15, -1)
    # )
    # depth_first_search(init_state, goal_state)
