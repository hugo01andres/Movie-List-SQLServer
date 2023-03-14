from pyodbc import connect

# CREATE CONNECTION
conn = connect('')

# CURSOR
cursor = conn.cursor()

# CREATE TABLES

CREATE_MOVIES_TABLE = """
IF NOT EXISTS (SELECT * FROM sysobjects WHERE name='movies' and xtype='U')
    CREATE TABLE movies (
    id INT IDENTITY(1,1) PRIMARY KEY,
    title VARCHAR(50),
    date_of_movie VARCHAR(12)
    );
"""
CREATE_USERS_TABLE = """
IF NOT EXISTS (SELECT * FROM sysobjects WHERE name='users' and xtype='U')
    CREATE TABLE users (
    username VARCHAR(50) PRIMARY KEY
    );
"""

CREATE_WATCHED_TABLE = """
IF NOT EXISTS (SELECT * FROM sysobjects WHERE name='watched' and xtype='U')
    CREATE TABLE watched(
    user_username VARCHAR(50),
    movie_id INT,
    FOREIGN KEY (user_username) REFERENCES users(username),
    FOREIGN KEY (movie_id) REFERENCES movies(id)
    );
"""

#  INSERT TO TABLES
INSERT_MOVIE = """
    INSERT INTO movies(title, date_of_movie) VALUES(?,?);"""

INSERT_WATCHED_MOVIE = "INSERT INTO watched(movie_id, user_username) VALUES(?,?)"
INSERT_USER = """INSERT INTO users(username) VALUES (?)"""

# SELECT TABLES
SELECT_MOVIES = """SELECT * FROM movies;"""
SELECT_WATCHED_MOVIES = """SELECT * FROM watched w
JOIN movies m
ON w.movie_id = m.id
JOIN users u
ON u.username = w.user_username
WHERE w.user_username = ?
"""


# CONVERT LIST O DICTIONARY
def to_dictionary(rows):
    pass


# CREATE TABLE FOR MOVIES
def create_table():    
    cursor.execute(CREATE_MOVIES_TABLE)
    cursor.execute(CREATE_USERS_TABLE)
    cursor.execute(CREATE_WATCHED_TABLE)
    conn.commit()


# ADD TABLES

# ADD MOVIES
def add_movie(title,date):
    cursor.execute(INSERT_MOVIE, (title,date))
    conn.commit()

# ADD WATCHED MOVIES
def watch_movie(username, movie_id):
    cursor.execute(INSERT_WATCHED_MOVIE, (movie_id,username))
    conn.commit()

# ADD USER
def add_user(user):
    cursor.execute(INSERT_USER, (user,))
    conn.commit()

# SEE ALL MOVIES
def view_all_movies():
    cursor.execute(SELECT_MOVIES)
    rows = cursor.fetchall()

    # get column names from cursor description
    col_names = [col[0] for col in cursor.description]

    # iterate over rows to create a list of dictionaries
    result = []
    for row in rows:
        d = dict(zip(col_names, row))
        result.append(d)
    return result

# MOVIES WATCHED
def view_movies_watched(username):
    cursor.execute(SELECT_WATCHED_MOVIES, (username,))
    rows = cursor.fetchall()

    # get column names from cursor description
    col_names = [col[0] for col in cursor.description]

    # iterate over rows to create a list of dictionaries
    result = []
    for row in rows:
        d = dict(zip(col_names, row))
        result.append(d)
    return result




# CLOSE CONNECTION
def close_connection():
    cursor.close()
    conn.close()
