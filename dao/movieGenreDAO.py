import json
import sqlite3
from typing import List
from core.rating import Rating
from core.movieGenre import MovieGenre

class MovieGenreDAO():

    # Constructor
    def __init__(self, prop_file:str) -> None:
        self.prop_file = prop_file
        # Get DB properties
        with open(prop_file, "r") as prop:
            content = json.loads(prop.read())
            dbURL = content["MovieGenre"]["dbURL"]
            self.tableName = content["MovieGenre"]["tableName"]
        # Connect to the database
        self.myConn = sqlite3.connect(dbURL)

        # print(f"DB connection successfull to {dbURL}")

    # Destructor
    def __del__(self) -> None:
        self.myConn.close()

    # Return a list of MovieGenre objects
    # containing all the rows present in the movie_gen table
    def getAllMovieGenres(self) -> List[MovieGenre]:
        output = []
        cursor = self.myConn.execute(f"SELECT * FROM {self.tableName}")
        for row in cursor:
            output.append(self.convertRowToMovieGenre(row))

        return output

    # Return a list of MovieGenre objects
    # containing movies seen by a user with userId as argument
    # for a single genre from user_movie_genre_info VIEW
    def searchMoviesSeenByUserBySingleGenre(self, userId:int, genreId:int) -> List[MovieGenre]:
        output = []
        query = '''
            SELECT movieId
            FROM user_movie_genre_info
            WHERE userId = {0} AND genreId = {1}
            
            EXCEPT
            
            SELECT movieId
            FROM user_movie_genre_info
            WHERE userId = {0} AND genreId != {1}
        '''.format(userId, genreId)
        cursor = self.myConn.execute(query)
        for row in cursor:
            new_row = list(row) + genreId
            output.append(self.convertRowToMovieGenre(new_row))
        return output

    # Return a list of MovieGenre objects
    # containing rows which have the genreId
    # column same as the argument
    def searchByGenreID(self, genreId:int) -> List[MovieGenre]:
        output = []
        cursor = self.myConn.execute(f"SELECT * FROM {self.tableName} WHERE genreId = {genreId}")
        for row in cursor:
            output.append(self.convertRowToMovieGenre(row))
        return output

    # Return a list of MovieGenre objects
    # containing rows which have the movieId
    # column same as the argument
    def searchByMovieID(self, movieId:int) -> List[MovieGenre]:
        output = []
        cursor = self.myConn.execute(f"SELECT * FROM {self.tableName} WHERE movieId = {movieId}")
        for row in cursor:
            output.append(self.convertRowToMovieGenre(row))
        return output

    # Return a list of MovieGenre objects
    # containing rows which have the movieId
    # column same as the argument list
    def searchByUserRatingList(self, ratingList:List[Rating]) -> List[MovieGenre]:
        output = []

        for rating in ratingList:
            movie_genres = self.searchByMovieID(rating.getMovieID())
            for movieGenre in movie_genres:
                output.append(movieGenre)

        return output

    # Return a MovieGenre object by converting
    # a row list of SQLite to MovieGenre(movieId, genreId)
    def convertRowToMovieGenre(self, row) -> MovieGenre:
        movieId = row[0]
        genreId = row[1]
        return MovieGenre(movieId, genreId)


if __name__ == "__main__":
    dao = MovieGenreDAO("../config/db_properties.json")

    print(dao.searchMoviesSeenByUserBySingleGenre(1, 3))

    # table = dao.getAllMovieGenres()

    # for row in table:
    #     print(row)

    # for movie_genre in dao.searchByGenreID(1):
    #     print(movie_genre)

    # for movie_genre in dao.searchByGenreID(1):
    #     print(movie_genre)

    # from core.rating import Rating

    # rating1 = Rating(1, 553, 5.0)

    # genres = dao.searchByUserRatingList(dao.searchByGenreID(1))

    # for genre in genres:
    #     print(genre)