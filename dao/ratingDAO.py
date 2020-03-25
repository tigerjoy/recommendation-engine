import json
import sqlite3
from core.rating import Rating

class RatingDAO():

    # Constructor
    def __init__(self, prop_file):
        self.prop_file = prop_file
        # Get DB properties
        with open(prop_file, "r") as prop:
            content = json.loads(prop.read())
            dbURL = content["Rating"]["dbURL"]
            self.tableName = content["Rating"]["tableName"]
        # Connect to the database
        self.myConn = sqlite3.connect(dbURL)

        print(f"DB connection successfull to {dbURL}")

    # Destructor
    def __del__(self):
        self.myConn.close()

    # Return a list of Rating objects
    # containing all the rows present in the rating table
    def getAllRating(self):
        output = []
        cursor = self.myConn.execute(f"SELECT * FROM {self.tableName}")
        for row in cursor:
            output.append(self.convertRowToRating(row))
        return output

    # Return a list of Rating objects
    # containing rows which have the movieId
    # column same as the argument
    def searchByMovieID(self, movieId):
        output = []
        cursor = self.myConn.execute(f"SELECT * FROM {self.tableName} WHERE movieId = {movieId}")
        for row in cursor:
            output.append(self.convertRowToRating(row))
        return output

    # Return a list of Rating objects
    # containing rows which have the userId
    # ciolumn same as the argument
    def searchByUserID(self, userId):
        output = []
        cursor = self.myConn.execute(f"SELECT * FROM {self.tableName} WHERE userId = {userId}")
        for row in cursor:
            output.append(self.convertRowToRating(row))
        return output

    # Return a Rating object by converting
    # a row list of SQLite to Rating(userId, movieId, rating)
    def convertRowToRating(self, row):
        userId = row[0]
        movieId = row[1]
        rating = row[2]


        return Rating(userId, movieId, rating)

if __name__ == "__main__":
    dao = RatingDAO("../config/db_properties.json")

    # table = dao.getAllRating()

    # count = 0
    # for row in table:
    #     print(row)
    #     count += 1
    #     if count == 20:
    #         break

    for row in dao.searchByUserID(1):
        print(row)

    # for movie in dao.searchByTitle("Toy"):
    #     print(movie)

    # for movie in dao.searchByGenre("Action"):
    #     print(movie)