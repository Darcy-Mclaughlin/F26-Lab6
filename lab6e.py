#!/usr/bin/env python3
# Author: Darcy McLaughlin
# Date: 4/11/2026
# Purpose: Traverse dictionary.
# Usage: ./lab6e.py

my_dict = {"switzerland" : "Alps", "United States" : "Alska Range", "Armenia" : "Caucasus", "Argentina" : "Andes", "Karakoram" : "Pakistan"}
# TO DO 1: Create a for in loop as instructed in readme.md file. 

# A dictionary is provided to you in ./lab6e.py file, use the for in loop and items() methodto traverse this dictionary and print the dictionary showing the following exact output.
for country, mountain_range in my_dict.items():
    print(f"{country}: {mountain_range}")

    
# TO DO 2: Run the script, and take the screenshot of code and output.
