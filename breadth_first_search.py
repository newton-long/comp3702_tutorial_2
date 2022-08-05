from queue import Queue
from typing import List

from PuzzleNode import PuzzleNode
from node_utils import backtrack_actions, state_to_tuple


def breadth_first_search(init_state: List, goal_state: List):
    goal_state = tuple([tuple(row) for row in goal_state])
    # Breadth-first Search
    print("Running Breadth-first Search...")
    visited = set()

    q = Queue[PuzzleNode]()
    q.put(PuzzleNode(None, None, init_state))

    while not q.empty():
        node = q.get()
        if node.current_state == goal_state:
            print("We reached the goal!")
            break
        if node.current_state not in visited:
            visited.add(node.current_state)

        for action in node.actions():
            new_state = node.step(action)
            if state_to_tuple(new_state) not in visited:
                q.put(PuzzleNode(node, action, new_state))

        # children = node.get_children()
        # for succ in children:
        #     if succ not in visited:
        #         q.put(succ)

    if q.empty():
        node = None

    return backtrack_actions(node, visited)


def breadth_first_search_original(init_state, goal_state):
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

    return backtrack_actions(node, visited)


