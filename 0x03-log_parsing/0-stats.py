#!/usr/bin/env python3

import sys
import signal

# Initialize variables
total_file_size = 0
status_code_counts = {}

# Define a signal handler to print statistics on keyboard interruption
def signal_handler(sig, frame):
    print_statistics()
    sys.exit(0)

# Print statistics
def print_statistics():
    print("File size:", total_file_size)
    for status_code in sorted(status_code_counts.keys()):
        count = status_code_counts[status_code]
        print(f"{status_code}: {count}")

# Register the signal handler for keyboard interruption (CTRL + C)
signal.signal(signal.SIGINT, signal_handler)

# Process each line from stdin
for line_number, line in enumerate(sys.stdin, start=1):
    try:
        # Parse the line
        ip_address, _, _, _, status_code, file_size = line.strip().split()[0:6]
        status_code = int(status_code)
        file_size = int(file_size)

        # Update total file size
        total_file_size += file_size

        # Update status code counts
        if status_code in status_code_counts:
            status_code_counts[status_code] += 1
        else:
            status_code_counts[status_code] = 1

        # Print statistics every 10 lines
        if line_number % 10 == 0:
            print_statistics()

    except ValueError:
        # Skip lines with incorrect format
        continue

# Print final statistics
print_statistics()
