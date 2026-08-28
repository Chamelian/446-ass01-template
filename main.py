# John Maynard
# CSCI 446 Fall 2026
# Programming Assignment #1
# I declare that I am the author of this work, take full responsibility for it, and have disclosed any material external assistance.

from random import choice, randint, sample
from time import sleep


class Vacuum:

    def __init__(self, position: tuple[int, int]) -> None:
        self.x: int = position[0]
        self.y: int = position[1]

    def suck(self, grid: list[list[int]]) -> None:
        if grid[self.x][self.y] != 1:  # Should never run
            raise ValueError
        else:
            grid[self.x][self.y] = 0

    def move(self, gridSize: int) -> None:
        directionOptions: list[int] = list(range(4))

        # Edge detection
        if self.x == 0:
            directionOptions.remove(3)
        elif self.x == gridSize - 1:
            directionOptions.remove(2)

        if self.y == 0:
            directionOptions.remove(0)
        elif self.y == gridSize - 1:
            directionOptions.remove(1)

        # Choose direction and move
        randomDirection: int = choice(directionOptions)
        match randomDirection:
            case 0:  # Up
                self.y -= 1
            case 1:  # Down
                self.y += 1
            case 2:  # Right
                self.x += 1
            case 3:  # Left
                self.x -= 1
            case _:  # Should never run
                raise ValueError


def vacuumVisualizer(
    grid: list[list[int]], vacuum: Vacuum, moveCounter: int, slowdown: float = 0.1
) -> None:
    # https://en.wikipedia.org/wiki/ANSI_escape_code#Control_Sequence_Introducer_commands
    # Used wikipedia for assistance with control codes
    # Resets the cursor to the beginning of the grid
    if moveCounter != 0:
        print(f"\033[{len(grid) + 1}A\r")

    # Slows down the display so it can be monitored
    sleep(slowdown)

    cleanSquare: str = "+"
    dirtySquare: str = "@"
    vacuumSquare: str = "V"
    for i in range(len(grid)):
        for j in range(len(grid)):
            if vacuum.x == j and vacuum.y == i:
                print(vacuumSquare, end=" ")
            elif grid[j][i] == 1:
                print(dirtySquare, end=" ")
            else:
                print(cleanSquare, end=" ")
        print()
    print(f"{moveCounter} moves", end="")


def vacuumSim(gridSize: int, dirtyWeight: int) -> int:
    grid: list[list[int]] = [[0] * gridSize for i in range(gridSize)]

    dirtyChoices: list[int] = sample(range((gridSize**2) - 1), dirtyWeight)
    for tile in dirtyChoices:
        tilePos: tuple[int, int] = divmod(tile, gridSize)
        grid[tilePos[0]][tilePos[1]] = 1

    dirtyTiles: int = dirtyWeight

    vacuum: Vacuum = Vacuum(divmod(randint(0, (gridSize**2) - 1), gridSize))

    moveCounter: int = 0
    while dirtyTiles > 0:
        vacuumVisualizer(grid, vacuum, moveCounter)
        if grid[vacuum.x][vacuum.y] == 1:
            vacuum.suck(grid)
            dirtyTiles -= 1
        else:
            vacuum.move(gridSize)

        moveCounter += 1

    return moveCounter


def main() -> None:
    print(f"\r{vacuumSim(5, 5)} moves")


if __name__ == "__main__":
    main()
