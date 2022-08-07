import time
from collections import deque
from typing import List, Tuple, Set

from PuzzleNode import PuzzleNode
from node_utils import backtrack_actions, state_to_tuple


def depth_first_search(init_state: Tuple[Tuple[int]], goal_state: Tuple[Tuple[int]]):
    t0 = time.time()
    goal_state = tuple([tuple(row) for row in goal_state])
    print("Running Depth-first Search...")
    visited = set[Tuple]()

    stack = deque[PuzzleNode]()
    stack.append(PuzzleNode(None, None, init_state))

    while stack:
        node = stack.pop()
        if node.current_state == goal_state:
            print("We reached the goal!")
            break

        visited.add(node.current_state)

        for action in node.actions():
            new_state = node.step(action)
            if new_state not in visited:
                stack.append(PuzzleNode(node, action, new_state))

    if not stack:
        node = None

    t_dfs = (time.time() - t0) / 1
    print(f'Finished in {t_dfs}s')

    return backtrack_actions(node, visited, False)

