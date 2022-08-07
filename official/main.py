from official.Node import Node
from official.bfs import breadth_first_search_original
from official.dfs import depth_first_search_original
from official.ucs import uniform_cost_search_original

if __name__ == '__main__':
    init_state = Node(["7", "2", "4", "5", "3", "6", "8", "_", "1"], None, None)
    goal_state = Node(["1", "2", "3", "4", "5", "6", "7", "8", "_"], None, None)

    breadth_first_search_original(init_state, goal_state)
    depth_first_search_original(init_state, goal_state)
    uniform_cost_search_original(init_state, goal_state)
