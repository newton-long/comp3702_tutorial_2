import time
from typing import List

from PuzzleNode import PuzzleNode
from node_utils import backtrack_actions, state_to_tuple


def depth_first_search(init_state: List, goal_state: List):
    t0 = time.time()
    goal_state = tuple([tuple(row) for row in goal_state])
    print("Running Depth-first Search...")
    visited = set()

    q = list[PuzzleNode]()
    q.append(PuzzleNode(None, None, init_state))

    while q:
        node = q.pop()
        if node.current_state == goal_state:
            print("We reached the goal!")
            break
        if node.current_state not in visited:
            visited.add(node.current_state)

        for action in node.actions():
            new_state = node.step(action)
            if state_to_tuple(new_state) not in visited:
                q.append(PuzzleNode(node, action, new_state))
    t_dfs = (time.time() - t0) / 1
    print(f'Finished in {t_dfs}s')

    return backtrack_actions(node, visited, False)

