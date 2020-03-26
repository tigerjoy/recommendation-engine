import json
import sqlite3
from typing import List
from core.averageRating import AverageRating

class AverageRatingDAO():

    # Constructor
    def __init__(self, prop_file:str) -> None:
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
    def __del__(self) -> None:
        self.myConn.close()

    # Return a list of AverageRating objects
    # containing all the rows present in the rating table
    def getAllAverageRatings(self) -> List[AverageRating]:
        output = []

        cursor = self.myConn.execute(f"SELECT * FROM {self.tableName}")

        for row in cursor:
            output.append(self.convertRowToAverageRating(row))

        return output

    # Return a list of AverageRating objects
    # containing rows which have the movieId
    # column same as the argument
    def searchByMovieID(self, movieId:int) -> List[AverageRating]:
        output = []
        cursor = self.myConn.execute(f"SELECT * FROM {self.tableName} WHERE movieId = {movieId}")
        for row in cursor:
            output.append(self.convertRowToAverageRating(row))
        return output

    # Return a Rating object by converting
    # a row list of SQLite to AverageRating(movieId, avgRating)
    def convertRowToAverageRating(self, row) -> AverageRating:
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