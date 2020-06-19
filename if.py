movies_watched = {"The Matrix", "Shawshank Redemption", "The Godfather", "Monty Python's Life of Brian"}
user_movie = input("Enter a film you watched recently: ")

if user_movie in movies_watched:
    print(f"I've watched {user_movie} too!")
else:
    print("I haven't watched that yet")