
# To get the actions to get here we can backtrack from the goal up the chain of parents.
from typing import Set, List

from PuzzleNode import PuzzleNode


def state_to_tuple(state: List):
    tuples = [tuple(row) for row in state]
    return tuple(tuples)


def backtrack_actions(goal_node:PuzzleNode, visited_nodes:Set):
    print("Visited nodes:", len(visited_nodes))
    if goal_node is not None:
        seq = [goal_node]
        node = goal_node
        # Initial node has no parent
        while node.parent:
            seq.append(node.parent)
            node = node.parent

        # Reverse it to get the correct order
        seq.reverse()
        print("Number of actions:", len(seq) - 1)
        # print("Total cost:", goal_node.total_cost)
        print("\nSOLUTION:\n")
        for s in seq:
            s.print()

        return seq
    else:
        print("UNSOLVABLE")
        return []
