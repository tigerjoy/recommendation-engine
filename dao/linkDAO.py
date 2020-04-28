import json
import sqlite3
from typing import List
from core.link import Link


class LinkDAO():

    # Constructor
    def __init__(self, prop_file: str) -> None:
        self.prop_file = prop_file
        # Get DB properties
        with open(prop_file, "r") as prop:
            content = json.loads(prop.read())
            dbURL = content["Link"]["dbURL"]
            self.tableName = content["Link"]["tableName"]
        # Connect to the database
        self.myConn = sqlite3.connect(dbURL)

        # print(f"DB connection successful to {dbURL}")

    # Destructor
    def __del__(self) -> None:
        self.myConn.close()

    # Return a list of Link objects
    # containing rows which have the movieId
    # column same as the argument
    def searchByMovieID(self, movieId: int) -> List[Link]:
        output = []
        cursor = self.myConn.execute(f"SELECT * FROM {self.tableName} WHERE movieId = {movieId}")
        for row in cursor:
            output.append(self.convertRowToLink(row))
        return output

    # Return a Genre object by converting
    # a row list of SQLite to Genre(genreId, genreName)
    def convertRowToLink(self, row) -> Link:
        movieId = row[0]
        imdbId = row[1]
        tmdbId = row[1]

        return Link(movieId, imdbId, tmdbId)
