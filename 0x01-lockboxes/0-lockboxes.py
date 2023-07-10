#!/usr/bin/python3
"""Lockboxes Contains method that finds the keys to
open other lockboxes
"""


def canUnlockAll(boxes):
    """
       Function that determines if you can open all the lockboxes
       Args:
           boxes: list of lists of integers
       Returns:
           True if you can open all the lockboxes, False otherwise
       """
    num_boxes = len(boxes)
    unlocked = set()
    unlocked.add(0)  # Start with the first box
    keys = boxes[0]  # Start with the keys from the first box
    while keys:
        key = keys.pop()
        if key < num_boxes and key not in unlocked:
            unlocked.add(key)
            keys.extend(boxes[key])

    return len(unlocked) == num_boxes
