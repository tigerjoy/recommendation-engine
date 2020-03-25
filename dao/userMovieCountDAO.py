import json
import sqlite3
from dao.genreDAO import GenreDAO
from core.userMovieCount import UserMovieCount

class UserMovieCountDAO():

    # Constructor
    def __init__(self, prop_file):
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
    def __del__(self):
        self.myConn.close()

    def getAllUserMovieCounts(self):
        output = []

        cursor = self.myConn.execute(f"SELECT * FROM {self.tableName}")

        for row in cursor:
            output.append(self.convertRowToUserMovieCount(row))

        return output

    def searchByUserIDGenreID(self, userId, genreId):
        gdDAO = GenreDAO(self.prop_file)

        # Obtaining the genreName from genreId
        genreName = gdDAO.searchByGenreID(genreId)[0].getGenreName()

        row = self.myConn.execute(f"SELECT userId, {genreName} FROM {self.tableName} WHERE userId = {userId}").fetchone()

        return row[1]

    def searchByUserIDGenreName(self, userId, genreName):
        row = self.myConn.execute(f"SELECT userId, {genreName} FROM {self.tableName} WHERE userId = {userId}").fetchone()

        return row[1]

    # Returns an UserMovieCount object
    def searchByUserID(self, userId):
        output = []

        cursor = self.myConn.execute(f"SELECT * FROM {self.tableName} WHERE userId = {userId}")

        for row in cursor:
            output.append(self.convertRowToUserMovieCount(row))

        return output

    def convertRowToUserMovieCount(self, row):
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

        return UserMovieCount(userId, Action, Adventure, Animation, Children, Comedy, Crime, Documentary, Drama, Fantasy, FilmNoir, Horror, IMAX, Musical, Mystery, Romance, SciFi, Thriller, War, Western)

if __name__ == "__main__":
    dao = UserMovieCountDAO("../config/db_properties.json")

    # table = dao.getAllGenres()

    # for row in table:
    #     print(row)

    print(dao.searchByUserID(1)[0])
