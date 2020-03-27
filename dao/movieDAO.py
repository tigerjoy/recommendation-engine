import json
import sqlite3
from typing import List
from core.movie import Movie

class MovieDAO():

    # Constructor
    def __init__(self, prop_file:str) -> None:
        self.prop_file = prop_file
        # Get DB properties
        with open(prop_file, "r") as prop:
            content = json.loads(prop.read())
            dbURL = content["Movie"]["dbURL"]
            self.tableName = content["Movie"]["tableName"]
        # Connect to the database
        self.myConn = sqlite3.connect(dbURL)

        # print(f"DB connection successfull to {dbURL}")

    # Destructor
    def __del__(self) -> None:
        self.myConn.close()

    # Return a list of Movie objects
    # containing all the rows present in the
    # movies_out table
    def getAllMovies(self) -> List[Movie]:
        output = []
        cursor = self.myConn.execute(f"SELECT * FROM {self.tableName}")
        for row in cursor:
            output.append(self.convertRowToMovie(row))

        return output

    # Return a list of Movie objects
    # containing rows which have the movieId
    # column same as the argument
    def searchByMovieID(self, movieId:int) -> List[Movie]:
        output = []
        cursor = self.myConn.execute(f"SELECT * FROM {self.tableName} WHERE movieId = {movieId}")
        for row in cursor:
            output.append(self.convertRowToMovie(row))
        return output

    # Return a list of Movie objects
    # containing rows which have the title
    # column similar to the argument
    def searchByTitle(self, title:str) -> List[Movie]:
        output = []
        cursor = self.myConn.execute(f"SELECT * FROM {self.tableName} WHERE title LIKE '%{title}%'")
        for row in cursor:
            output.append(self.convertRowToMovie(row))
        return output

    # Return a list of Movie objects
    # containing rows which contain the
    # argument in the genre column
    def searchByGenre(self, genre:str) -> List[Movie]:
        output = []
        cursor = self.myConn.execute(f"SELECT * FROM {self.tableName} WHERE genres LIKE '%{genre}%'")
        for row in cursor:
            output.append(self.convertRowToMovie(row))
        return output

    # Return a Movie object by converting
    # a row list of SQLite to Movie(movieId, title, genres)
    def convertRowToMovie(self, row) -> Movie:
        movieId = row[0]
        title = row[1]
        genres = row[2]
        return Movie(movieId, title, genres)


if __name__ == "__main__":
    dao = MovieDAO("../config/db_properties.json")

    table = dao.getAllMovies()

    count = 0
    for row in table:
        print(row)
        count += 1
        if count == 20:
            break

    # print(dao.searchByMovieID(3))

    # for movie in dao.searchByTitle("Toy"):
    #     print(movie)

    # for movie in dao.searchByGenre("Action"):
    #     print(movie)