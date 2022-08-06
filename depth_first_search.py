from typing import List

from PuzzleNode import PuzzleNode
from node_utils import backtrack_actions, state_to_tuple


def depth_first_search(init_state: List, goal_state: List):
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

    return backtrack_actions(node, visited, True)

def depth_first_search_original(init_state, goal_state):
    print("Running Depth-first Search...")
    visited = set()

    st = list()
    st.append(init_state)

    while st:
        node = st.pop()
        if node == goal_state:
            print ("We reached the goal!")
            break
        if node not in visited:
            visited.add(node)

        children = node.get_children()
        for succ in children:
            if succ not in visited:
                st.append(succ)

    if not st:
        node = None

    return backtrack_actions(node, visited)
