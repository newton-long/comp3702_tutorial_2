
# To get the actions to get here we can backtrack from the goal up the chain of parents.
from typing import Set, List, Tuple

from PuzzleNode import PuzzleNode


def state_to_tuple(state: List):
    tuples = [tuple(row) for row in state]
    return tuple(tuples)


# sum of for each tile t, the number of tiles with higher number that is placed behind it
def get_inversion_count(state_1_d: Tuple):
    inv_count = 0
    empty_value = -1
    for i in range(0, len(state_1_d)):
        for j in range(i + 1, len(state_1_d)):
            if state_1_d[j] != empty_value and state_1_d[i] != empty_value and state_1_d[i] > state_1_d[j]:
                inv_count += 1
    return inv_count

def backtrack_actions(goal_node: PuzzleNode, visited_nodes: Set, print_progress: bool = False):
    print("Visited nodes:", len(visited_nodes))
    if goal_node is not None:
        seq = [goal_node]
        node = goal_node
        total_cost = node.cost

        # Initial node has no parent
        while node.parent:
            seq.append(node.parent)
            total_cost += node.parent.cost
            node = node.parent

        # Reverse it to get the correct order
        seq.reverse()
        print("Number of actions:", len(seq) - 1)
        print("Total cost:", total_cost)
        if print_progress:
            print("\nSOLUTION:\n")
            for s in seq:
                s.print()

        return seq
    else:
        print("UNSOLVABLE")
        return []
