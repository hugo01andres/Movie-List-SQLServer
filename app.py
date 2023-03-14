from db import create_table, add_movie , view_all_movies , add_user , watch_movie , view_movies_watched

# WELCOME
def welcome():
    print("Welcome to the watchlist app\n\n")

# MENU
def menu():
    print("""
    1) ADD MOVIE.\n
    2) VIEW ALL MOVIES.\n
    3) WATCH A MOVIE\n
    4) VIEW WATCHED MOVIES.\n
    5) ADD USER.\n
    6) EXIT
    """)
    return input("\nOption:")

# PRINT MOVIES
def print_movies(movies):
    for movie in movies:
        print(f"Title: {movie['title']} DATE: {movie['date_of_movie']}")

# PROGRAMM FUCNTIONS

# 1) ADD MOVIES
def add_movies_app():
    title = input("Title: ")
    date = input("dd/mm/YYYY: ")
    add_movie(title, date)


# 2) VIEW ALL MOVIES
def view_all_movies_app(movies):
    print_movies(movies)

# 3) WATCH A MOVIE
def watch_movie_app():
    user_name = input("Enter your username: ")
    movie_id = input("Enter movie_id: ")
    watch_movie(user_name,movie_id)
    print("Watching a movie...")

# 4) VIEW WATCHED MOVIES
def view_watched_movies_app(movies):
    for movie in movies:
        print(f"Title: {movie['title']} USER: {movie['user_username']}")
    

# 5) ADD USER
def add_user_app():
    user_name = input("Enter your username: ")
    add_user(user_name)



# ----------------------MAIN--------------------------

def main():
    # CREATE 3 TABLES
    create_table()
    # START THE PROGRAM
    while(user_input := menu()) != '6':
        # 1) Add new movie
        if user_input == "1":
            add_movies_app()
        # 2) View all movies
        elif user_input == "2":
            view_all_movies_app(view_all_movies())
        # 3) Add watched movie
        elif user_input == "3":
            watch_movie_app()
        # 4) View watched movies
        elif user_input == "4":
            user_name = input("Enter your username: ")
            view_watched_movies_app(view_movies_watched(user_name))
        # 5) ADD USER
        elif user_input == "5":
            add_user_app()
        else:
            print("\nInvalid Option, Please Try Again\n\n")

if __name__ == '__main__':
    main()
