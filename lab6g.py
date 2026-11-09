#!/usr/bin/env python3
# Author: Darcy McLaughlin
# Date: 4/11/2026
# Purpose: Use Dictionary for Structured Data.
# Usage: ./lab6g.py

#In your lab6g.py file create a function named add_movie() which adds a new movie object into a movie database.
# The database is a list, and each movie object in the list is a dictionary. The dictionary should contain the following keys (name, director, year, runtime).
# The values attached to these keys should be pass as arguments to the function.
# Call the function 4 times with 4 different movies.
# In the main() function print the database with each movie data printed on a single line.
# Run the script from command line using the command: python ./lab6g.py.
# Note that this is a complex task, you are creating a list of dictionaries. It is a really useful concept and if you are able to write this script, you should be proud of you!
# TO DO 1: Create function add_movie(). 

def add_movie(movie_database, title, director, year):
    movie_database[title] = {
        'director': director,
        'year': year
    }

    
# TO DO 2: Call the function 4 times.

movie_db = {}
add_movie(movie_db, "The Matrix", "The Wachowskis", 1999)
add_movie(movie_db, "Inception", "Christopher Nolan", 2010)
add_movie(movie_db, "Interstellar", "Christopher Nolan", 2014)
add_movie(movie_db, "The Dark Knight", "Christopher Nolan", 2008)

# TO DO 3: Print the database as instructed in readme.md file.

for title, details in movie_db.items():
    print(f"Title: {title}, Director: {details['director']}, Year: {details['year']}")
    

# TO DO 4: Run the script. Take screenshot of code and script.
