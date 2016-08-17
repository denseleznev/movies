#!/usr/bin/env python

"""Movie Trailer Website"""

import media
import fresh_tomatoes

# Create our favorite movie objects
ace_ventura = media.Movie("Ace Ventura: Pet Detective",
                          "https://upload.wikimedia.org/wikipedia/en/8/84/Ace_ventura_pet_detective.jpg",
                          "https://www.youtube.com/watch?v=QzxDlS6QY1s")
green_mile = media.Movie("The Green Mile",
                         "https://upload.wikimedia.org/wikipedia/en/c/ce/Green_mile.jpg",
                         "https://www.youtube.com/watch?v=ctRK-4Vt7dA")
shawshank = media.Movie("The Shawshank Redemption",
                        "https://upload.wikimedia.org/wikipedia/en/8/81/ShawshankRedemptionMoviePoster.jpg",
                        "https://www.youtube.com/watch?v=6hB3S9bIaco")
smith = media.Movie("Mr. & Mrs. Smith",
                    "https://upload.wikimedia.org/wikipedia/en/b/b4/Mr_and_mrs_smith_poster.jpg",
                    "https://www.youtube.com/watch?v=7C1miwFdQOQ")
pets = media.Movie("The Secret Life of Pets",
                   "https://upload.wikimedia.org/wikipedia/en/6/64/The_Secret_Life_of_Pets_poster.jpg",
                   "https://www.youtube.com/watch?v=UZ4WBlveGfw")
button = media.Movie("The Curious Case of Benjamin Button",
                     "https://upload.wikimedia.org/wikipedia/en/7/7d/Curious_case_of_benjamin_button_ver3.jpg",
                     "https://www.youtube.com/watch?v=VqeqaweXBV0")

# Here we have to make a list of our movie objects because fresh_tomatoes
# requires a list of objects as an argument
movies = [ace_ventura, green_mile, shawshank, smith, pets, button]

# Send a list to fresh_tomatoes, which will generate beautiful HTML page
fresh_tomatoes.open_movies_page(movies)
