from core.movieCycle import MovieCycle
import json
import sqlite3


class MovieCycleDAO:

    # Constructor
    def __init__(self, prop_file: str) -> None:
        self.prop_file = prop_file
        # Get DB properties
        with open(prop_file, "r") as prop:
            content = json.loads(prop.read())
            dbURL = content["MovieCycle"]["dbURL"]
            self.tableName = content["MovieCycle"]["tableName"]
        # Connect to the database
        self.myConn = sqlite3.connect(dbURL)

        # print(f"DB connection successful to {dbURL}")

    # Returns the row corresponding to user_id as a MovieCycle object
    def getRecordByUser(self, user_id: int) -> MovieCycle:
        query = f"""
                    SELECT *
                    FROM {self.tableName}
                    WHERE user_id = {user_id}
                """
        cursor = self.myConn.execute(query).fetchone()
        return self.convertRowToMovieCycle(cursor)

    def addRecord(self, the_record: MovieCycle) -> bool:
        query = f"""
                    INSERT INTO '{self.tableName}'('user_id', 'last_movie_id', 'second_last_movie_id') 
                    VALUES (?, ?, ?);
                """

        data_tuple = (the_record.getUserID(), the_record.getLastMovieID(), the_record.getSecondLastMovieID())

        self.myConn.execute(query, data_tuple)

        self.myConn.commit()

        return self.myConn.total_changes > 0


    def deleteRecordByUser(self, user_id: int) -> bool:
        query = f"""
                    DELETE FROM {self.tableName}
                    WHERE user_id = {user_id}
                """
        self.myConn.execute(query)
        self.my_conn.commit()

        return self.myConn.total_changes > 0

    def updateRecordByUser(self, user_id: int, last_movie_id: int, second_last_movie_id) -> bool:
        query = f"""
                    UPDATE {self.tableName}
                    SET last_movie_id = {last_movie_id},
                        second_last_movie_id = {second_last_movie_id}
                    WHERE user_id = {user_id}
                """
        self.myConn.execute(query)
        self.my_conn.commit()

        return self.myConn.total_changes > 0

    def convertRowToMovieCycle(self, row):
        user_id = row[0]
        last_movie_id = row[1]
        second_last_movie_id = row[2]

        return MovieCycle(user_id, last_movie_id, second_last_movie_id)
