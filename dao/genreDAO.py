import json
import sqlite3
from typing import List
from core.genre import Genre

class GenreDAO():

    # Constructor
    def __init__(self, prop_file:str) -> None:
        self.prop_file = prop_file
        # Get DB properties
        with open(prop_file, "r") as prop:
            content = json.loads(prop.read())
            dbURL = content["Genre"]["dbURL"]
            self.tableName = content["Genre"]["tableName"]
        # Connect to the database
        self.myConn = sqlite3.connect(dbURL)

        # print(f"DB connection successfull to {dbURL}")

    # Destructor
    def __del__(self) -> None:
        self.myConn.close()

    # Return a list of Genre objects
    # containing all the rows present in the
    # genid_gen table
    def getAllGenres(self) -> List[Genre]:
        output = []
        cursor = self.myConn.execute(f"SELECT * FROM {self.tableName}")
        for row in cursor:
            output.append(self.convertRowToGenre(row))
        return output

    # Return a list of Genre objects
    # containing rows which have the genreId
    # column same as the argument
    def searchByGenreID(self, genreId:int) -> List[Genre]:
        output = []
        cursor = self.myConn.execute(f"SELECT * FROM {self.tableName} WHERE genreId = {genreId}")
        for row in cursor:
            output.append(self.convertRowToGenre(row))
        return output

    # Return a list of Genre objects
    # containing rows which have the genreName
    # column same as the argument
    def searchByGenreName(self, genreName:str) -> List[Genre]:
        output = []
        cursor = self.myConn.execute(f"SELECT * FROM {self.tableName} WHERE genreName = {genreName}")
        for row in cursor:
            output.append(self.convertRowToGenre(row))
        return output

    # Return a Genre object by converting
    # a row list of SQLite to Genre(genreId, genreName)
    def convertRowToGenre(self, row) -> Genre:
        genreId = row[0]
        genreName = row[1]

        return Genre(genreId, genreName)


if __name__ == "__main__":
    dao = GenreDAO("../config/db_properties.json")

    table = dao.getAllGenres()
    # output = ""

    i = 0
    for row in table:
        print(f"{row.getGenreName()}, ", end="")
        i += 1

    # print(output.strip())
    # output = ""

    # for genre in dao.getAllGenres():
    #     genreName = genre.getGenreName()
    #     output += "\n'\\n" + genreName + ": " + "{}'" + ".format(self.get" + genreName + "Count()) + \\".replace("-", "")

    # print(output)

    # print(dao.searchByMovieID(163981))
