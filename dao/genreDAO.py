import json
import sqlite3
from core.genre import Genre

class GenreDAO():

    # Constructor
    def __init__(self, prop_file):
        self.prop_file = prop_file
        # Get DB properties
        with open(prop_file, "r") as prop:
            content = json.loads(prop.read())
            dbURL = content["Genre"]["dbURL"]
            self.tableName = content["Genre"]["tableName"]
        # Connect to the database
        self.myConn = sqlite3.connect(dbURL)

        print(f"DB connection successfull to {dbURL}")

    # Destructor
    def __del__(self):
        self.myConn.close()

    def getAllGenres(self):
        output = []

        cursor = self.myConn.execute(f"SELECT * FROM {self.tableName}")

        for row in cursor:
            output.append(self.convertRowToGenre(row))

        return output

    def searchByGenreID(self, genreId):
        output = []
        cursor = self.myConn.execute(f"SELECT * FROM {self.tableName} WHERE genreId = {genreId}")
        for row in cursor:
            output.append(self.convertRowToGenre(row))
        return output

    def searchByGenreName(self, genreName):
        output = []
        cursor = self.myConn.execute(f"SELECT * FROM {self.tableName} WHERE genreName = {genreName}")
        for row in cursor:
            output.append(self.convertRowToGenre(row))
        return output


    def convertRowToGenre(self, row):
        genreId = row[0]
        genreName = row[1]

        return Genre(genreId, genreName)

if __name__ == "__main__":
    dao = GenreDAO("../config/db_properties.json")

    table = dao.getAllGenres()

    for row in table:
        print(row)

    # output = ""

    # for genre in dao.getAllGenres():
    #     genreName = genre.getGenreName()
    #     output += "\n'\\n" + genreName + ": " + "{}'" + ".format(self.get" + genreName + "Count()) + \\".replace("-", "")

    # print(output)

    # print(dao.searchByMovieID(163981))