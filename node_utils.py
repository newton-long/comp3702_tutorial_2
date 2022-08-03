
# To get the actions to get here we can backtrack from the goal up the chain of parents.
def backtrack_actions(goal_node, visited_nodes):
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
        print("Total cost:", goal_node.total_cost)
        print("\nSOLUTION:\n")
        for s in seq:
            s.print(str(s.previous_action))
    else:
        print("UNSOLVABLE")
