import json
import sqlite3
from core.movieGenre import MovieGenre

class MovieGenreDAO():

    # Constructor
    def __init__(self, prop_file):
        self.prop_file = prop_file
        # Get DB properties
        with open(prop_file, "r") as prop:
            content = json.loads(prop.read())
            dbURL = content["MovieGenre"]["dbURL"]
            self.tableName = content["MovieGenre"]["tableName"]
        # Connect to the database
        self.myConn = sqlite3.connect(dbURL)

        print(f"DB connection successfull to {dbURL}")

    # Destructor
    def __del__(self):
        self.myConn.close()

    # Return a list of MovieGenre objects
    # containing all the rows present in the movie_gen table
    def getAllMovieGenres(self):
        output = []
        cursor = self.myConn.execute(f"SELECT * FROM {self.tableName}")
        for row in cursor:
            output.append(self.convertRowToMovieGenre(row))

        return output

    # Return a list of MovieGenre objects
    # containing rows which have the genreId
    # column same as the argument
    def searchByGenreID(self, genreId):
        output = []
        cursor = self.myConn.execute(f"SELECT * FROM {self.tableName} WHERE genreId = {genreId}")
        for row in cursor:
            output.append(self.convertRowToMovieGenre(row))
        return output

    # Return a list of MovieGenre objects
    # containing rows which have the movieId
    # column same as the argument
    def searchByMovieID(self, movieId):
        output = []
        cursor = self.myConn.execute(f"SELECT * FROM {self.tableName} WHERE movieId = {movieId}")
        for row in cursor:
            output.append(self.convertRowToMovieGenre(row))
        return output

    # Return a MovieGenre object by converting
    # a row list of SQLite to MovieGenre(movieId, genreId)
    def convertRowToMovieGenre(self, row):
        movieId = row[0]
        genreId = row[1]


        return MovieGenre(movieId, genreId)

if __name__ == "__main__":
    dao = MovieGenreDAO("../config/db_properties.json")

    # table = dao.getAllMovieGenres()

    # for row in table:
    #     print(row)

    for movie_genre in dao.searchByGenreID(1):
        print(movie_genre)