import heapq
import time
from typing import List, Tuple, Set

from PuzzleNode import PuzzleNode
from node_utils import backtrack_actions, state_to_tuple


def uniform_cost_search(init_state: Tuple[Tuple[int]], goal_state: Tuple[Tuple[int]]):
    t0 = time.time()
    goal_state = tuple([tuple(row) for row in goal_state])
    print("Running Uniform-cost Search...")
    visited = set[Tuple]()

    heap = [PuzzleNode(None, None, init_state)]
    heapq.heapify(heap)

    while heap:
        node = heapq.heappop(heap)
        if node.current_state == goal_state:
            print("We reached the goal!")
            break

        for action in node.actions():
            new_state = node.step(action)
            if new_state not in visited:
                visited.add(new_state)

                new_node = PuzzleNode(node, action, new_state)
                new_node.cost += node.cost

                heapq.heappush(heap, new_node)

    t_dfs = (time.time() - t0) / 1
    print(f'Finished in {t_dfs}s')

    return backtrack_actions(node, visited, False)

