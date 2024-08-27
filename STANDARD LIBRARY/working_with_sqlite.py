# sqlite is a very light database that is used to store data of an application
import sqlite3
import json
from pathlib import Path


movies = json.loads(Path("movies.json").read_text())
# print(movies)

with sqlite3.connect("db.sqlite3") as conn:
    # command = "INSERT INTO Movies VALUES(?,?,?)"
    command = "SELECT* FROM Movies"
    for movie in movies:
        # conn.execute(command, tuple(movie.values()))
        cursor = conn.execute(command)
        # for row in cursor:
        #     print(row)
        movies = cursor.fetchall()
        print(movies)
    # conn.commit()
