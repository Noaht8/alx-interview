#!/usr/bin/python3

def canUnlockAll(boxes):
  """
  Determines if all the boxes can be opened.

  Args:
    boxes: A list of lists, where each inner list represents the keys to unlock
      the other boxes.

  Returns:
    True if all boxes can be opened, else False.
  """

  # Initialize a set to track the boxes that have been unlocked.
  unlocked = {0}

  # Iterate over all the boxes.
  for box in boxes:
    # Add any unlocked boxes to the set.
    for key in box:
      if key in unlocked:
        unlocked.add(key)

  # Return True if all the boxes have been unlocked.
  return len(unlocked) == len(boxes)
