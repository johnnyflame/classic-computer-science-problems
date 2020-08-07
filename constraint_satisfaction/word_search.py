from typing import NamedTuple, List, Dict, Optional
from random import choice
from string import ascii_uppercase
from CSP_solver import CSP, Constraint

# Type alias for grid
Grid = List[List[str]]


class GridLocation(NamedTuple):
    row: int
    column: int


def generate_grid(row: int, columns: int) -> Grid:
    return [[choice(ascii_uppercase) for c in range(columns)] for r in range(rows)]


def display_grid(grid: Grid) -> None:
    for row in grid:
        print("".join(row))

