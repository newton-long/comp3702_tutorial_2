import time

from official.Node import backtrack_actions


def depth_first_search_original(init_state, goal_state):
    t0 = time.time()
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

    t_dfs = (time.time() - t0) / 1
    print(f'Finished in {t_dfs}s')

    return backtrack_actions(node, visited)
