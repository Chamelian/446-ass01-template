# Task: Simple Vacuum Cleaner Simulation
__Objective__: Create a simulation of a simple vacuum cleaner agent operating in a two-dimensional environment to clean dirty tiles.
Description:
1.	__Environment__:
•	A two-dimensional grid, for example, 5x5, where each cell can be either clean or dirty.
•	Initially, assign the "dirty" state to a few random cells.
•	The vacuum cleaner starts at a random position on the grid.
2.	__Vacuum Cleaner Actions__:
•	The vacuum cleaner can perform the following actions: suck (clean the current cell), move left, move right, move up, move down.
•	The vacuum cleaner operates based on simple reactive rules:
•	If the current cell is dirty, it cleans the cell (suck).
•	If the cell is clean, it moves in a random direction.
3.	__Vacuum Cleaner Goal__:
•	The ultimate goal is to reach a state where all cells are clean.
•	The task ends when the vacuum cleaner achieves this state.
__Hints for Developers__:
•	Start by creating the grid model and implementing the basic actions for the vacuum cleaner.
•	Implement the reactive logic according to the defined rules.
•	An optional final step could be to add a simple interface for visualizing the vacuum cleaner's actions.
