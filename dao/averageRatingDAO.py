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
            # print("DBURL =", dbURL)
            self.tableName = content["AverageRating"]["tableName"]
        # Connect to the database
        self.myConn = sqlite3.connect(dbURL)

        # print(f"DB connection successfull to {dbURL}")

    # Destructor
    def __del__(self) -> None:
        self.myConn.close()

    # Return a list of AverageRating objects
    # containing all the rows present in the rating table
    # in ascending order of average rating if ascending is True,
    # in descending order of average rating otherwise
    def getAllAverageRatings(self, ascending: bool) -> List[AverageRating]:
        output = []
        order = "ASC" if ascending else "DESC";
        query = f"""
                    SELECT *
                    FROM {self.tableName}
                    ORDER BY avgRating {order}
                """
        cursor = self.myConn.execute(query)

        for row in cursor:
            output.append(self.convertRowToAverageRating(row))

        return output

    # Return a list of AverageRating objects
    # for those movies which belong to genreIds
    # and have been seen by user with userId argument
    # Uses the user_info VIEWS
    def moviesSeenByUser(self, genreIds: List[int], userId: int, ascending: bool = True):
        # Forming the SQL query
        order = "ASC" if ascending else "DESC";
        column_name = "genreId"
        genre_comma_seperated = "( " + str(genreIds[0])
        genreIds_length = len(genreIds)
        for i in range(1, genreIds_length):
            genre_comma_seperated += ", {}".format(genreIds[i])
        genre_comma_seperated += " )"
        # Generating intersect query
        template = '''
                    SELECT movieId, avgRating
                    FROM user_info
                    WHERE {} = {} AND userId = {}
                '''
        query_start = ''
        query_start += template.format(column_name, genreIds[0], userId)
        for i in range(1, len(genreIds)):
            query_start += '''
                    INTERSECT
                    {}'''.format(template.format(column_name, genreIds[i], userId))
        query_end = '''
                    EXCEPT 

                    SELECT movieId, avgRating
                    FROM user_info
                    WHERE {0} NOT IN {1} AND userId = {2}

                    ORDER BY avgRating {3};
                '''.format(column_name, genre_comma_seperated, userId, order)
        query = query_start + query_end
        # print(query)
        cursor = self.myConn.execute(query)
        # Generating output list
        output = []
        for row in cursor:
            output.append(self.convertRowToAverageRating(row))
        return output

    # Return a list of AverageRating objects
    # containing only those rows for movies
    # belonging to genreIds argument
    # Uses the movie_info VIEW which is a join
    # between tables average_rating and movie_gen
    def moviesFromGenres(self, genreIds: List[int], ascending: bool) -> List[AverageRating]:
        # Forming the SQL query
        order = "ASC" if ascending else "DESC";
        column_name = "genreId"
        genre_comma_seperated = "( " + str(genreIds[0])
        genreIds_length = len(genreIds)
        for i in range(1, genreIds_length):
            genre_comma_seperated += ", {}".format(genreIds[i])
        genre_comma_seperated += " )"
        # Generating intersect query
        template = '''
            SELECT movieId, avgRating
            FROM movie_info
            WHERE {} = {}
        '''
        query_start = ''
        query_start += template.format(column_name, genreIds[0])
        for i in range(1, len(genreIds)):
            query_start += '''
            INTERSECT
            {}'''.format(template.format(column_name, genreIds[i]))
        query_end = '''
            EXCEPT 
            
            SELECT movieId, avgRating
            FROM movie_info
            WHERE {0} NOT IN {1}
            
            ORDER BY avgRating {2};
        '''.format(column_name, genre_comma_seperated, order)
        query = query_start + query_end
        # print(query)
        cursor = self.myConn.execute(query)
        # Generating output list
        output = []
        for row in cursor:
            output.append(self.convertRowToAverageRating(row))
        return output

    # Add a average rating entry for a movie
    def addAverageRatingByMovie(self, the_avg_rating: AverageRating) -> bool:
        query = f"""
                    INSERT INTO '{self.tableName}' ('movieId', 'avgRating') 
                    VALUES (?, ?);
                """

        data_tuple = (the_avg_rating.getMovieID(), the_avg_rating.getAverageRating())

        self.myConn.execute(query, data_tuple)

        self.myConn.commit()

        return self.myConn.total_changes > 0

    # Update the average rating entry for a movie
    def updateAverageRatingByMovie(self, the_avg_rating: AverageRating) -> bool:
        query = f'''
                    UPDATE {self.tableName}
                    SET avgRating = {the_avg_rating.getAverageRating()}
                    WHERE movieId = {the_avg_rating.getMovieID()}
                 '''
        self.myConn.execute(query)
        self.myConn.commit()
        return self.myConn.total_changes == 1

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
    def convertRowToAverageRating(self, row, is_join_operation:bool = False) -> AverageRating:
        movieId = row[0]
        avgRating = row[1]

        return AverageRating(movieId, avgRating);


if __name__ == "__main__":
    dao = AverageRatingDAO("../config/db_properties.json")
    # table = dao.getAllAverageRatings()

    # for row in table:
    #     print(row.getMovieID(), row.getAverageRating())

    # dao.moviesNotSeenByUser([3, 2, 4], 5, False);

    # dao.selectFromJoin([1, 2, 4], False)

    # for row in dao.selectFromJoin([1, 2], False):
    #     print(row)

    for row in dao.moviesNotSeenByUser([1, 2], 1, False):
        print(row)

    # print(len(dao.moviesNotSeenByUser([1, 2], 1, False)))

    # result = dao.searchByMovieID(22)
    # for row in result:
    #     print(row.getAverageRating())