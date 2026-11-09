#!/usr/bin/env python3
# Author: Darcy McLaughlin
# Date: 4/11/2026
# Purpose: Use Dictionary for Structured Data.
# Usage: ./lab6h.py

# TO DO 1: Copy the code from lab6g.py and paste here.
def add_movie(movie_database, title, director, year):
    movie_database[title] = {
        'director': director,
        'year': year
    }

    movie_db = {}
add_movie(movie_db, "The Matrix", "The Wachowskis", 1999)
add_movie(movie_db, "Inception", "Christopher Nolan", 2010)
add_movie(movie_db, "Interstellar", "Christopher Nolan", 2014)
add_movie(movie_db, "The Dark Knight", "Christopher Nolan", 2008)

for title, details in movie_db.items():
    print(f"Title: {title}, Director: {details['director']}, Year: {details['year']}")
    

# TO DO 2: Create function find_movie().

def find_movie(movie_database, title):
    if title in movie_database:
        details = movie_database[title]
        return f"Title: {title}, Director: {details['director']}, Year: {details['year']}"
    else:
        return "Movie not found."
    
# TO DO 3: Call the function as instructed in readme.md file.

print(find_movie(movie_db, "Inception"))
print(find_movie(movie_db, "The Godfather"))

# TO DO 4: Run the script. Take screenshot of code and script.

