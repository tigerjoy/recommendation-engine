import json
import sqlite3
from core.averageRating import AverageRating

class AverageRatingDAO():

    # Constructor
    def __init__(self, prop_file):
        self.prop_file = prop_file
        # Get DB properties
        with open(prop_file, "r") as prop:
            content = json.loads(prop.read())
            dbURL = content["AverageRating"]["dbURL"]
            print("DBURL =", dbURL)
            self.tableName = content["AverageRating"]["tableName"]
        # Connect to the database
        self.myConn = sqlite3.connect(dbURL)

        print(f"DB connection successfull to {dbURL}")

    # Destructor
    def __del__(self):
        self.myConn.close()

    def getAllAverageRatings(self):
        output = []

        cursor = self.myConn.execute(f"SELECT * FROM {self.tableName}")

        for row in cursor:
            output.append(self.convertRowToAverageRating(row))

        return output

    def searchByMovieID(self, movieId):
        output = []
        cursor = self.myConn.execute(f"SELECT * FROM {self.tableName} WHERE movieId = {movieId}")
        for row in cursor:
            output.append(self.convertRowToAverageRating(row))
        return output


    def convertRowToAverageRating(self, row):
        movieId = row[0]
        avgRating = row[1]

        return AverageRating(movieId, avgRating)

if __name__ == "__main__":
    dao = AverageRatingDAO("../config/db_properties.json")
    # table = dao.getAllAverageRatings()

    # for row in table:
    #     print(row.getMovieID(), row.getAverageRating())

    result = dao.searchByMovieID(22)
    for row in result:
        print(row.getAverageRating())