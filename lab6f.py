#!/usr/bin/env python3
# Author: Darcy McLaughlin
# Date: 4/11/2026
# Purpose: Use Dictionary for Problem solving.
# Usage: ./lab5f.py

# TO DO 1: Create function histogram() as instructed in readme.md file.

def histogram(s):
    d = dict()
    for c in s:
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1
    return d


# TO DO 2: Create main() function and call histogram(). Call the main() function.

def main():
    s = input("Enter a string: ")
    hist = histogram(s)
    print(hist)

__main__ = "__main__"
if __name__ == __main__:
    main()
    
# TO DO 3: Run the script. Take screenshot of code showing the functions histogram() and main(). Also show output in the screenshot.
