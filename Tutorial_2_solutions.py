#!/usr/bin/env python
# coding: utf-8

# # Tutorial 2

# Let us recall the components we need for an agent.
# - Action Space (A)
# - Percept Space (P) 
# - State Space (S)
# - Transition Function (T : S x A -> S')
# - Utility Function (U: S -> R)
# 
# We know the problem is fully observable, thus the percept space is the same as the state space and we dont need to do anything special while considering it. For BFS and DFS problems there is no cost associated with actions, the utility will therefore become 1 for reaching the goal state and 0 otherwise.
# 
# That leaves us with action space, state space, and transition function.
# 
# In the 8-puzzle game there are 4 actions that are available to us, Up, Right, Down, Left. These 4 actions make up the action space, the actions are not all always available, however we will worry about that when getting to the transition function.
# 
# The transition function is the core of the problem, given a state and an action we need a way to find the next state. The implementation for this will largely depend on the state space, so let's start with that. 
#   

# ## State Representation
# 
# Let's start by defining the state space in terms of Python code. There are a few things we will be interested in. 
# - The grid layout: What numbers are in what positions? We will treat this as a list, however there are a number of ways we can model it
# - What action led to here?
# - What was the previous state?
# - Whether the cell visited or not
# 
# To keep track of all these properties, let's start by defining a class.
# 
# We'll also keep track of the cost. This is not needed for BFS and DFS, however is very important when we get to UCS.

# In[15]:


# We'll need this later for Uniform Cost Search
from queue import *
import heapq

# We'll need this to copy states
import copy


# In[16]:


# State representation
class Node:
    def __init__(self, grid, previous_action, parent):
        self.grid = grid
        self.previous_action = previous_action
        self.parent = parent
        self.total_cost = 0 # For UCS


# We'll be using two coordinate systems to represent states:
# 
# A linear index state state space for 8-puzzle:
# We'll use this to store the game state in `self.grid`, as it is compact.
# ```
# +---+---+---+
# | 0 | 1 | 2 |
# +---+---+---+
# | 3 | 4 | 5 | 
# +---+---+---+
# | 6 | 7 | 8 |
# +---+---+---+
# ```
# 
# A 2-tuple (2D) index:
# This is easier when moving tiles around.
# ```
# +-----+-----+-----+
# |(0,0)|(1,0)|(2,0)|
# +-----+-----+-----+
# |(0,1)|(1,1)|(2,1)|
# +-----+-----+-----+
# |(0,2)|(1,2)|(2,2)|
# +-----+-----+-----+
# ```
# 
# We can write helper functions to:
# - Convert between these representations
# - To check whether a given position is valid
# - Whether two states are equal (as well a hash function to this effect)
# - Print out what a state looks like

# In[17]:


class Node(Node): # Continued
    @staticmethod
    def to_1d(x, y):
        return (3 * y) + x

    @staticmethod
    def to_2d(i):
        return i % 3, i // 3
    
    @staticmethod
    def is_valid_pos_2d(x, y):
        return 0 <= x and x < 3 and 0 <= y and y < 3
    
    # Override equality and hash - needed to check when 2 states are equal
    # It would otherwise default to checking object references
    def __eq__(self, other):
        return self.grid == other.grid
    
    def __hash__(self):
        return hash(tuple(self.grid))
    
    def print(self, description):
        print(description);
        for y in range(3):
            for x in range(3):
                print("{:^3}".format(str(self.grid[self.to_1d(x, y)])), end='')
            print()
        print()
    


# Within these positions, we can store strings representing each tile (`"_"` for the blank tile) for the blank tile. For example,
# ```
# +-----+-----+-----+
# | "7" | "2" | "4" |
# +-----+-----+-----+
# | "5" | "3" | "6" |
# +-----+-----+-----+
# | "8" | "_" | "1" |
# +-----+-----+-----+
# ```
# To get the index of the blank tile, we do the following:

# In[18]:


class Node(Node): # Continued
    def get_blank_i(self):
        return self.grid.index("_")


# Next, the transition function, we need to do 2 things here. Firstly we need to check that the action given is valid, and second we need to perform the action.
# 
# We can check if the action is valid by getting the current index of the tile. We try moving the tile in each of the four directions (actions) and test whether it is in a valid location (i.e. within the board). If this is the case, we swap the blank tile with whatever is in the new position.
# 
# While we are making children, we keep track of the childs parent and the action that led to the child.

# In[19]:


class Node(Node): # Continued
    @staticmethod
    def get_blank_tile_neighbours(x, y):
        """
        Takes blank tile coordinates and for every action in A returns where it would go.
        """
        return {'L': (x - 1, y),
                'R': (x + 1, y),
                'U': (x, y - 1),
                'D': (x, y + 1)}

    def get_children(self):
        # Current blank tile location
        i_old = self.get_blank_i()
        x_old, y_old = self.to_2d(i_old)
        
        # Neighbouring blank tile locations
        neighbours = self.get_blank_tile_neighbours(x_old, y_old)
        
        # For valid neighbouring positions, swap the tiles around
        children = list()
        for a, n in neighbours.items():
            x_new, y_new = n[0], n[1]
            if self.is_valid_pos_2d(x_new, y_new):
                succ_state = copy.deepcopy(self.grid) # We don't want to ruin the previous state's grid
                i_new = self.to_1d(x_new, y_new)
                succ_state[i_old], succ_state[i_new] = succ_state[i_new], succ_state[i_old]
                succ = Node(succ_state, a, self)
                children.append(succ)
                
        return children


# This is all the basics we need for our state and transition components. Now we need to perform our search.
# 
# ## Breadth-first Search
# 
# For testing, let's create an initial state and a goal state.
# We'll also need some way to keep track of states that were already visited, so well make a set for that.
# 

# In[20]:


init_state = Node(["7", "2", "4", "5", "3", "6", "8", "_", "1"], None, None)
goal_state = Node(["1", "2", "3", "4", "5", "6", "7", "8", "_"], None, None)

init_state.print("Initial state")
goal_state.print("Goal state")

init_children = init_state.get_children();
for child in init_children:
    child.print("Init child: {}".format(child.previous_action))
    
# Breadth-first Search
print("Running Breadth-first Search...")
visited = set()


# We'll also start with BFS, so well need to create a queue, and well put our initial state into it.

# In[21]:


q = Queue()
q.put(init_state)


# Now lets start our search, recall that the basic structure of search is to take items out of the queue, get its successors, and put them into the queue. We also need to keep track of visited states, so we don't go around in circles.

# In[22]:


while not q.empty():
    node = q.get()
    if node == goal_state:
        print ("We reached the goal, Jolly Good!")
        break;
    if node not in visited:
        visited.add(node)

    children = node.get_children()
    for succ in children:
        if succ not in visited:
            q.put(succ)
            
if(q.empty()):
    node = None


# To get the actions to get here we can backtrack from the goal up the chain of parents.

# In[23]:


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
        
backtrack_actions(node, visited)


# ## Depth-first Search
# 
# To change it to DFS, we just have to recall that DFS uses a stack, so we would switch over the queue in the code above to a stack and we're done.

# In[24]:


# Depth-first Search
def depth_first_search(init_state, goal_state):
    print("Running Depth-first Search...")
    visited = set()

    st = list()
    st.append(init_state)

    while st:
        node = st.pop()
        if node == goal_state:
            print ("We reached the goal, Jolly Good!")
            break;
        if node not in visited:
            visited.add(node)

        children = node.get_children()
        for succ in children:
            if succ not in visited:
                st.append(succ)

    if not st:
        node = None

    return node, visited


# ## Uniform Cost Search
# 
# The last part is to convert our BFS code to UCS. The difference here is that UCS keeps track of the cost of actions. We are given that the cost of actions is {Up=1, Down=2, Left=3, Right=4}. In other words, going up 4 times is as expensive as going right once. We are no longer concerned with minimising the number of moves, instead we want to minimize the cost.
# 
# Let's add this to our representation of the game:

# In[25]:


class Node(Node): # Continued
    # Returns cost of making an action
    def get_cost(self):
        if(self.previous_action == 'U'):
            return 1
        elif(self.previous_action == 'D'):
            return 2
        elif(self.previous_action == 'L'):
            return 3
        elif(self.previous_action == 'R'):
            return 4
        else:
            raise Exception("Invalid action: {}".format(self.action))
    
    # Override less than function for UCS
    def __lt__(self, other):
        return self.total_cost < other.total_cost


# In our Node class above we keep track of the aggregate cost from the start position to each new state. To make use of this we will use a priority queue (`heapq`), which takes elements out that have the smallest cost.
# 
# You'll notice we also made function `__lt__`, this is an override for the less than operator (<), which we will use for UCS to compare the total cost of two states.

# In[26]:


# Uniform Cost Search
def uniform_cost_search(init_state, goal_state):
    print("Running Uniform Cost Search...")
    visited = set()

    pq = []
    pq.append(init_state)
    heapq.heapify(pq)

    while pq:
        node = heapq.heappop(pq)
        if node == goal_state:
            print ("We reached the goal, Jolly Good!")
            break;
        if node not in visited:
            visited.add(node)

        children = node.get_children()
        for succ in children:
            if succ not in visited:
                # Calculate total cost and add to unexplored nodes
                succ.total_cost = node.total_cost + succ.get_cost()
                heapq.heappush(pq, succ)

    if not pq:
        node = None
        
    return node, visited
        
goal_node, visited = uniform_cost_search(init_state, goal_state)
backtrack_actions(goal_node, visited)


# Notice that very little changed from the previous code, we replaced the queue with the heapq. The heapq will always take the item with the lowest value from the queue. Since we overrode the less than `__lt__` operator in our class, the `heapq` knows how to compare the elements.

# # Parity

# In[27]:


class Node(Node): # Continued
    def parity(self):
        total = 0
        grid_order = copy.deepcopy(self.grid)
        grid_order.remove("_")
        for i in range(len(grid_order)):
            for j in range(i + 1, len(grid_order)):
                if grid_order[j] < grid_order[i]:
                        total += 1
        if total % 2 == 0:
            parity = "even"
        else:
            parity = "odd"
        return parity, total

ex_1 = Node(["7", "2", "4", "5", "_", "6", "8", "3", "1"], None, None)
ex_2 = Node(["7", "2", "4", "5", "3", "6", "8", "_", "1"], None, None)
ex_3 = Node(["1", "2", "3", "4", "5", "6", "7", "8", "_"], None, None)
ex_4 = Node(["1", "2", "3", "4", "5", "6", "_", "8", "7"], None, None)

ex_1.print("Parity: {}".format(ex_1.parity()))
ex_2.print("Parity: {}".format(ex_2.parity()))
ex_3.print("Parity: {}".format(ex_3.parity()))
ex_4.print("Parity: {}".format(ex_4.parity()))

goal_node, visited = depth_first_search(ex_3, ex_4)
backtrack_actions(goal_node, visited)

