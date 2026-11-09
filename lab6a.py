#!/usr/bin/env python3
# Author: Darcy McLaughlin
# Date: 4/11/2026
# Purpose: Create Sets.
# Usage: ./lab6a.py

# TO DO 1: Complete the functions below.

#s3 which contains numbers between 0 and 100 which are divisible by 3.
# s5 which contains numbers between 0 and 100 which are divisible by 5.
# s7 which contains numbers between 0 and 100 which are divisible by 7.
# s11 which contains numbers between 0 and 100 which are divisible by 11

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

# TO DO 2: Run the script. Take screenshot of only buildtheSet() function. No need to capture main() in the screenshot. 
