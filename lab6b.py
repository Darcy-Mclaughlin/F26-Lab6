#!/usr/bin/env python3
# Author: Darcy McLaughlin
# Date: 4/11/2026
# Purpose: Practice Set Operations.
# Usage: ./lab6b.py

# TO DO 1: Copy the code from lab6a.py and paste here.

def buildtheSet(divisor):
    s = set()
    for i in range(0, 101):
        if i % divisor == 0:
            s.add(i)
    return s
def main():

    s3 = buildtheSet(3)
    print("s3: ", s3)
    print("----------------------------------------")

    s5 = buildtheSet(5)
    print("s5: ", s5)
    print("----------------------------------------")

    s7 = buildtheSet(7)
    print("s7: ", s7)
    print("----------------------------------------")

    s11 = buildtheSet(11)
    print("s11: ", s11)

main()

def s3ors5():
    s3 = buildtheSet(3)
    s5 = buildtheSet(5)
    return s3 | s5

def main():
    print("s3 or s5: ", s3ors5())

main()
# TO DO 2: Create the function s3ors5().
# TO DO 3: Run the script. Take screenshot of only s3ors5() function. No need to capture main() in the screenshot. Make sure you show the output in the screenshot.
