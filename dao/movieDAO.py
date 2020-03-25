import json
import sqlite3
from core.movie import Movie

class MovieDAO():

    # Constructor
    def __init__(self, prop_file):
        self.prop_file = prop_file
        # Get DB properties
        with open(prop_file, "r") as prop:
            content = json.loads(prop.read())
            dbURL = content["Movie"]["dbURL"]
            self.tableName = content["Movie"]["tableName"]
        # Connect to the database
        self.myConn = sqlite3.connect(dbURL)

        print(f"DB connection successfull to {dbURL}")

    # Destructor
    def __del__(self):
        self.myConn.close()

    def getAllMovies(self):
        output = []
        cursor = self.myConn.execute(f"SELECT * FROM {self.tableName}")
        for row in cursor:
            output.append(self.convertRowToMovie(row))

        return output

    def searchByMovieID(self, movieId):
        output = []
        cursor = self.myConn.execute(f"SELECT * FROM {self.tableName} WHERE movieId = {movieId}")
        for row in cursor:
            output.append(self.convertRowToMovie(row))
        return output

    def searchByTitle(self, title):
        output = []
        cursor = self.myConn.execute(f"SELECT * FROM {self.tableName} WHERE title LIKE '%{title}%'")
        for row in cursor:
            output.append(self.convertRowToMovie(row))
        return output

    def searchByGenre(self, genre):
        output = []
        cursor = self.myConn.execute(f"SELECT * FROM {self.tableName} WHERE genres LIKE '%{genre}%'")
        for row in cursor:
            output.append(self.convertRowToMovie(row))
        return output


    def convertRowToMovie(self, row):
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