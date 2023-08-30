#!/usr/bin/python3
"""Island perimeter computing module.
"""


def island_perimeter(grid):
    """Computes the perimeter of an island with no lakes.
    """
    perimeter = 0
    rows = len(grid)
    cols = len(grid[0])

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:  # Check if current cell is land
                perimeter += 4  # Add 4 to the perimeter count

                # Check the neighboring cells
                if i > 0 and grid[i - 1][j] == 1:  # Check cell above
                    perimeter -= 2  # Subtract 2 from the perimeter count
                if j > 0 and grid[i][j - 1] == 1:  # Check cell to the left
                    perimeter -= 2  # Subtract 2 from the perimeter count

    return perimeter
