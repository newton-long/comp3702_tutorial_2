# Official Solutions

These are the solutions from the Google Drive.

I split the Tutorial_2_solutions.py into separate files.

### Running

1) Nick's solution

    python official/tutorial2_nick.py

2) Solutions from Tutorial_2_solutions

    python official/main.py

### Comments

Nick's solution has a memory leak in DFS - the memory runs to ~16GB.

The other solution hard-codes magic numbers (resulting in static methods that would otherwise be instance method) 
and it's all set only for 8-puzzle.
The conversion between 1D and 2D is probably also unnecessary.