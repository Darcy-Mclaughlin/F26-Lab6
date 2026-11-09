#!/usr/bin/env python3
# Author: Darcy McLaughlin
# Date: 4/11/2026
# Purpose: Creating dictionary.
# Usage: ./lab6d.py

# In your lab6d.py file Create a function named times_ten(start_index: int, end_index: int), which creates and returns a new dictionary.
# The keys of the dictionary should be the numbers between start_index and end_index inclusive.
# The value mapped to each key should be the key times ten.
# The function prints the exact output as:

# TO DO 1: Create function times_ten as instructed in readme.md file. 

def times_ten(start_index: int, end_index: int):
    result = {}
    for i in range(start_index, end_index + 1):
        result[i] = i * 10
    return result
# TO DO 2: Run the script.
def main():
    print("times_ten(1, 5): ", times_ten(1, 5))

main()

