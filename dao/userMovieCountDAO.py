import json
import sqlite3
from typing import List
from dao.genreDAO import GenreDAO
from core.userMovieCount import UserMovieCount

class UserMovieCountDAO():

    # Constructor
    def __init__(self, prop_file:str) -> None:
        self.prop_file = prop_file
        # Get DB properties
        with open(prop_file, "r") as prop:
            content = json.loads(prop.read())
            dbURL = content["UserMovieCount"]["dbURL"]
            self.tableName = content["UserMovieCount"]["tableName"]
        # Connect to the database
        self.myConn = sqlite3.connect(dbURL)

        print(f"DB connection successfull to {dbURL}")

    # Destructor
    def __del__(self) -> None:
        self.myConn.close()

    # Return a list of UserMovieCount objects
    # containing all the rows present in the
    # user_movie_genre_wise_count table
    def getAllUserMovieCounts(self) -> List[UserMovieCount]:
        output = []

        cursor = self.myConn.execute(f"SELECT * FROM {self.tableName}")

        for row in cursor:
            output.append(self.convertRowToUserMovieCount(row))

        return output

    # Return a list of UserMovieCount objects
    # containing rows which have userId and genreId
    # column same as the argument
    def searchByUserIDGenreID(self, userId:int, genreId:int) -> List[UserMovieCount]:
        gdDAO = GenreDAO(self.prop_file)

        # Obtaining the genreName from genreId
        genreName = gdDAO.searchByGenreID(genreId)[0].getGenreName()

        row = self.myConn.execute(f"SELECT userId, {genreName} FROM {self.tableName} WHERE userId = {userId}").fetchone()

        return row[1]

    # Return an integer which is the count of the number
    # of movies watched by userId of genreName
    def searchByUserIDGenreName(self, userId:int, genreName:str) -> int:
        row = self.myConn.execute(f"SELECT userId, {genreName} FROM {self.tableName} WHERE userId = {userId}").fetchone()

        return row[1]

    # Returns a list of UserMovieCount objects
    # containing rows which have userId column
    # same as the argument
    def searchByUserID(self, userId:int) -> List[UserMovieCount]:
        output = []

        cursor = self.myConn.execute(f"SELECT * FROM {self.tableName} WHERE userId = {userId}")

        for row in cursor:
            output.append(self.convertRowToUserMovieCount(row))

        return output

    # Return a UserMovieCount object by converting
    # a row list of SQLite to UserMovieCount(userId, Action, ...)
    def convertRowToUserMovieCount(self, row) -> UserMovieCount:
        userId = row[0]
        Action = row[1]
        Adventure = row[2]
        Animation = row[3]
        Children = row[4]
        Comedy = row[5]
        Crime = row[6]
        Documentary = row[7]
        Drama = row[8]
        Fantasy = row[9]
        FilmNoir = row[10]
        Horror = row[11]
        IMAX = row[12]
        Musical = row[13]
        Mystery = row[14]
        Romance = row[15]
        SciFi = row[16]
        Thriller = row[17]
        War = row[18]
        Western = row[19]

        return UserMovieCount(userId, Action, Adventure, Animation, Children, Comedy, Crime, Documentary, Drama,
                              Fantasy, FilmNoir, Horror, IMAX, Musical, Mystery, Romance, SciFi, Thriller, War, Western)


if __name__ == "__main__":
    dao = UserMovieCountDAO("../config/db_properties.json")

    # table = dao.getAllGenres()

    # for row in table:
    #     print(row)

    # print(dao.searchByUserIDGenreName(1, "Action"))

    for user in dao.searchByUserID(1):
        print(user)
