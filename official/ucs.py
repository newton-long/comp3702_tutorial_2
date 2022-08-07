import heapq
import time
from queue import Queue

from official.Node import backtrack_actions


def uniform_cost_search_original(init_state, goal_state):
    t0 = time.time()

    init_state.print("Initial state")
    goal_state.print("Goal state")

    init_children = init_state.get_children()
    for child in init_children:
        child.print("Init child: {}".format(child.previous_action))

    # Breadth-first Search
    print("Running Uniform Cost Search...")
    visited = set()

    pq = []
    pq.append(init_state)
    heapq.heapify(pq)

    while pq:
        node = heapq.heappop(pq)
        if node == goal_state:
            print ("We reached the goal!")
            break
        if node not in visited:
            visited.add(node)

        children = node.get_children()
        for succ in children:
            if succ not in visited:
                # Calculate total cost and add to unexplored nodes
                succ.total_cost = node.total_cost + succ.get_cost()
                heapq.heappush(pq, succ)

    if not pq:
        node = None

    t_dfs = (time.time() - t0) / 1
    print(f'Finished in {t_dfs}s')

    return backtrack_actions(node, visited)


