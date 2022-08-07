import time
from queue import Queue
from typing import List, Tuple

from PuzzleNode import PuzzleNode
from node_utils import backtrack_actions, state_to_tuple


def breadth_first_search(init_state: Tuple[Tuple[int]], goal_state: Tuple[Tuple[int]]):
    t0 = time.time()
    goal_state = goal_state
    print("Running Breadth-first Search...")
    visited = set[Tuple]()

    q = Queue[PuzzleNode]()
    q.put(PuzzleNode(None, None, init_state))

    while not q.empty():
        node = q.get()

        if node.current_state == goal_state:
            print("We reached the goal!")
            break

        for action in node.actions():
            new_state = node.step(action)
            if new_state not in visited:
                visited.add(new_state)
                q.put(PuzzleNode(node, action, new_state))

    if q.empty():
        node = None

    t_dfs = (time.time() - t0) / 1
    print(f'Finished in {t_dfs}s')

    return backtrack_actions(node, visited)

