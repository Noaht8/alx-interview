#!/usr/bin/python3
"""Function to determine the winner of each game by passing 
the number of rounds (x) and the array of n values.
"""


def isWinner(x, nums):
    """Function to check if a number is prime"""
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    """Function to get the next prime number after a given number"""
    def get_next_prime(start):
        num = start + 1
        while not is_prime(num):
            num += 1
        return num

    """Function to play the game for a given value of n"""
    def play_game(n):
        primes = []  # List to store the prime numbers chosen by the players
        num = 1
        while num <= n:
            prime = get_next_prime(num)  # Get the next prime number
            primes.append(prime)  # Add the prime number to the list
            num = prime
            # Remove the prime number and its multiples from the set of numbers
            for i in range(prime, n + 1, prime):
                if i in nums:
                    nums.remove(i)

    maria_wins = 0  # Counter for Maria's wins
    ben_wins = 0  # Counter for Ben's wins

    # Iterate over each value of n
    for n in nums:
        play_game(n)  # Play the game for the current value of n
        # Determine the winner based on the remaining numbers
        if len(nums) % 2 == 0:
            ben_wins += 1
        else:
            maria_wins += 1

    # Determine the player with the most wins
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
