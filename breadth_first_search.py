from queue import Queue

from node_utils import backtrack_actions

def breadth_first_search(init_state, goal_state):
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

    backtrack_actions(node, visited)
