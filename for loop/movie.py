'''
#Ask first friend the movies they like. Save it in a list
#Ask another friend the same question. If the movie is in the first friend's list, 
#Print "You both like "name of the movie"
#Continue until they is atleast 3 movies they both like
'''
# Ask the first friend for the movies they like and save it in a list
first_friend_movies = input("First friend, what movies do you like? (Enter a list separated by commas): ").split(',')

# Ask the second friend for movies and check if they match with the first friend's list
common_movies = []
common_movie_count = 0  # Initialize a counter for common movies
attempts = 0  # Initialize a counter for the number of attempts by the second friend

while common_movie_count < 3 and attempts < 5:
    movie = input("Second friend, what movie do you like? (Enter one at a time): ").strip()
    attempts += 1
    
    # Check if the movie is in the first friend's list
    if movie in first_friend_movies:
        common_movies.append(movie)
        common_movie_count += 1  # Increment the common movie counter
        print(f"You both like '{movie}'!")
    else:
        print("Try again.")

# Print the list of common movies
if common_movie_count >= 3:
    print("You both like the following movies:")
    for movie in common_movies:
        print(f"- {movie}")
else:
    print("You didn't find 3 common movies, or the second friend reached 5 attempts.")
