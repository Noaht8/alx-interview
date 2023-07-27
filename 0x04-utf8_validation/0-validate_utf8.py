#!/usr/bin/python3
"""UTF-8 validation module.
"""


def validUTF8(data):
    """Checks if a list of integers are valid UTF-8 codepoints."""

    # Number of bytes in the current character
    num_bytes = 0

    for byte in data:
        # Check if the byte is a continuation byte
        if byte & 0b11000000 == 0b10000000:
            # If it's not a valid continuation byte, return False
            if num_bytes == 0:
                return False
            # Decrement the number of bytes remaining
            num_bytes -= 1
        else:
            # Check the number of bytes in the current character
            if num_bytes > 0:
                return False
            # Determine the number of bytes in the current character
            if byte & 0b10000000 == 0:
                num_bytes = 0
            elif byte & 0b11100000 == 0b11000000:
                num_bytes = 1
            elif byte & 0b11110000 == 0b11100000:
                num_bytes = 2
            elif byte & 0b11111000 == 0b11110000:
                num_bytes = 3
            else:
                return False

    # If there are remaining bytes, return False
    if num_bytes > 0:
        return False

    return True
