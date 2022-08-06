import time
from queue import Queue

from official.Node import backtrack_actions


def breadth_first_search_original(init_state, goal_state):
    t0 = time.time()
    
    init_state.print("Initial state")
    goal_state.print("Goal state")

    init_children = init_state.get_children()
    for child in init_children:
        child.print("Init child: {}".format(child.previous_action))

    # Breadth-first Search
    print("Running Breadth-first Search...")
    visited = set()

    q = Queue()
    q.put(init_state)


    while not q.empty():
        node = q.get()
        if node == goal_state:
            print("We reached the goal!")
            break
        if node not in visited:
            visited.add(node)

        children = node.get_children()
        for succ in children:
            if succ not in visited:
                q.put(succ)

    if (q.empty()):
        node = None

    t_dfs = (time.time() - t0) / 1
    print(f'Finished in {t_dfs}s')

    return backtrack_actions(node, visited)


