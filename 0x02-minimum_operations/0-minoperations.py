#!/usr/bin/python3
"""Module which contains minoperations function"""

def minOperations(n):
    """
  Calculates the fewest number of operations needed to result in exactly n H characters in the file.

  Args:
    n: The number of H characters to be in the file.

  Returns:
    The fewest number of operations needed.
  """

    operations = 0  # keep track of the number of operations.
    summation = 1   # represent the current number of characters in the file
    carrier = 0     # represent the number of characters in the clipboard.

    while summation < n:
        if n % summation == 0:  # Copy when summation is a multiple of n
            carrier = summation
            summation *= 2
            operations += 1
        else:
            summation += carrier
        operations += 1  # Always paste

    return operations
