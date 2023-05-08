'''Bonus
Movie Ratings Analysis
Scenario: You have just been hired as a data analyst at a movie streaming platform. Your manager has given you a list of movies, each with a tuple containing the movie title, release year, and user ratings. The platform allows users to rate movies on a scale of 1 to 10. Your manager wants you to create a Python program that:

Accepts a list of movies, with each movie represented as a tuple containing the movie title, release year, and a list of user ratings.
Calculates the average rating for each movie.
Filters out movies with an average rating lower than 6.0.
Displays the movies, along with their title, release year, and average rating.
Example input:

movies = [
    ("The Shawshank Redemption", 1994, [9, 10, 10, 9, 8, 9]),
    ("The Godfather", 1972, [10, 9, 8, 10, 9, 7]),
    ("Pulp Fiction", 1994, [9, 8, 7, 8, 6, 5]),
    ("The Dark Knight", 2008, [10, 9, 9, 8, 9, 8]),
    ("Schindler's List", 1993, [8, 9, 9, 7, 6, 8]),
    ("The Room", 2003, [1, 2, 3, 4, 5, 1])
]
Expected output:

1. The Shawshank Redemption (1994) - Avergae rating: 9.17 ★
2. The Godfather (1972) - Avergae rating: 8.83 ★
3. The Dark Knight (2008) - Avergae rating: 8.83 ★
4. Schindler's List (1993) - Avergae rating: 7.83 ★
5. Pulp Fiction (1994) - Avergae rating: 7.17 ★'''
Movies=[("The Shawshank Redemption", 1994, [9, 10, 10, 9, 8, 9]),
    ("The Godfather", 1972, [10, 9, 8, 10, 9, 7]),
    ("Pulp Fiction", 1994, [9, 8, 7, 8, 6, 5]),
    ("The Dark Knight", 2008, [10, 9, 9, 8, 9, 8]),
    ("Schindler's List", 1993, [8, 9, 9, 7, 6, 8]),
    ("The Room", 2003, [1, 2, 3, 4, 5, 1])]
print("please enter the name of the movie you watched:")
watchedMovie=input()
print(f"please give me your rate for{watchedMovie} ")
rate=input()
if watchedMovie=="The Godfather":
     MyNewTuble="The Shawshank Redemption", 1994, [9, 10, 10, 9, 8, 9,rate]
elif watchedMovie=="Pulp Fiction":
    MyNewTuble="Pulp Fiction", 1972, [10, 9, 8, 10, 9, 7,rate]
elif  watchedMovie=="The Dark Knight":
     MyNewTuble="The Dark Knight", 2008, [10, 9, 9, 8, 9, 8,rate]
elif watchedMovie=="Schindler's List":
     MyNewTuble="Schindler's List", 1993, [8, 9, 9, 7, 6, 8,rate]
elif watchedMovie=="The Room":
     MyNewTuble="The Room", 2003, [1, 2, 3, 4, 5, 1,rate]
i=0
for i in 6:
    theRate= MyNewTuble[i]
    avg=sum(theRate)/7
'''output
The Shawshank Redemption (1994) - Avergae rating: 9.17 ★
2. The Godfather (1972) - Avergae rating: 8.83 ★
3. The Dark Knight (2008) - Avergae rating: 8.83 ★
4. Schindler's List (1993) - Avergae rating: 7.83 ★
5. Pulp Fiction (1994) - Avergae rating: 7.17 ★'''
i=0
for i in 6:
     print(f"the{Movies[i]} ({Movies[i+1]}) - Average rating:{avg}*")

