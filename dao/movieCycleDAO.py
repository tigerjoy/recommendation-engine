from core.movieCycle import MovieCycle
import json
import sqlite3
from typing import List

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
    def getRecordByUserPriority(self, user_id: int, priority: int) -> List[MovieCycle]:
        output = []
        query = f"""
                    SELECT *
                    FROM {self.tableName}
                    WHERE user_id = {user_id}
                    AND priority = {priority}
                """
        cursor = self.myConn.execute(query)
        for row in cursor:
            output.append(self.convertRowToMovieCycle(row))
        return output

    #  Adds a record in the table
    def addRecord(self, the_record: MovieCycle) -> bool:
        query = f"""
                    INSERT INTO '{self.tableName}'('user_id', 'last_movie_id', 'second_last_movie_id', 'priority') 
                    VALUES (?, ?, ?, ?);
                """

        data_tuple = (the_record.getUserID(), the_record.getLastMovieID(), the_record.getSecondLastMovieID(),
                      the_record.getPriority())

        self.myConn.execute(query, data_tuple)

        self.myConn.commit()

        return self.myConn.total_changes > 0

    # Delete a record from the table
    def deleteRecordByUser(self, user_id: int) -> bool:
        query = f"""
                    DELETE FROM {self.tableName}
                    WHERE user_id = {user_id}
                """
        self.myConn.execute(query)
        self.myConn.commit()

        return self.myConn.total_changes > 0

    # Update a record in the table
    def updateRecordByUser(self, the_record: MovieCycle) -> bool:
        last_movie_id = the_record.getLastMovieID()
        second_last_movie_id = the_record.getSecondLastMovieID()
        user_id = the_record.getUserID()
        priority = the_record.getPriority()
        query = f"""
                    UPDATE {self.tableName}
                    SET last_movie_id = {last_movie_id},
                        second_last_movie_id = {second_last_movie_id}
                    WHERE user_id = {user_id}
                    AND priority = {priority}
                """
        self.myConn.execute(query)
        self.myConn.commit()

        return self.myConn.total_changes > 0

    # Helper method to convert row to MovieCycle object
    def convertRowToMovieCycle(self, row) -> MovieCycle:
        user_id = row[0]
        last_movie_id = row[1]
        second_last_movie_id = row[2]
        priority = row[1]

        return MovieCycle(user_id, last_movie_id, second_last_movie_id, priority)
