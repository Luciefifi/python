# sqlite is a very light database that is used to store data of an application
import sqlite3
import json
from pathlib import Path


movies = json.loads(Path("movies.json").read_text())
# print(movies)

with sqlite3.connect("db.sqlite3") as conn:
    command = "INSERT INTO Movues VALUES(?,?,?)"
    for movie in movies:
        conn.commit(command, tuple(movie.values()))
    conn.commit()
