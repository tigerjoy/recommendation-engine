import json
import sqlite3
from typing import List
from core.recommendation import Recommendation


class RecommendationDAO():

    # Constructor
    def __init__(self, prop_file: str) -> None:
        self.prop_file = prop_file
        # Get DB properties
        with open(prop_file, "r") as prop:
            content = json.loads(prop.read())
            dbURL = content["Recommendation"]["dbURL"]
            self.tableName = content["Recommendation"]["tableName"]
        # Connect to the database
        self.myConn = sqlite3.connect(dbURL)

        # print(f"DB connection successfull to {dbURL}")

    # Destructor
    def __del__(self) -> None:
        self.myConn.close()

    # Return a list of Recommendation objects
    # containing all the rows present in the recommendation table
    def getAllRecommendation(self) -> List[Recommendation]:
        output = []
        cursor = self.myConn.execute(f"SELECT * FROM {self.tableName}")
        for row in cursor:
            output.append(self.convertRowToRecommendation(row))
        return output

    # Returns the recommendation of the user
    def getRecommendationByUser(self, user_id: int) -> List[Recommendation]:
        output = []
        query = f"""
                    SELECT *
                    FROM {self.tableName}
                    WHERE user_id = {user_id}
                """
        cursor = self.myConn.execute(query)
        for row in cursor:
            output.append(self.convertRowToRecommendation(row))
        return output

    # Adds an entry in the table
    def addRecommendation(self, the_recommendation: Recommendation):
        query = f"""
                        INSERT INTO '{self.tableName}'('user_id', 'priority', 'genre_id') 
                        VALUES (?, ?, ?);
                        """

        data_tuple = (the_recommendation.getUserID(), the_recommendation.getPriority(),
                      the_recommendation.getGenreID())

        self.myConn.execute(query, data_tuple)

        self.myConn.commit()

        return self.myConn.total_changes > 0

    # Deletes an entry from the table
    def deleteRecommendation(self, the_recommendation: Recommendation):
        query = f"""
                    DELETE FROM {self.tableName}
                    WHERE user_id = {the_recommendation.getUserID()}
                    AND priority = {the_recommendation.getPriority()}
                """
        self.myConn.execute(query)

        self.myConn.commit()

        return self.myConn.total_changes > 0

    # Return a Rating object by converting
    # a row list of SQLite to Rating(userId, movieId, rating)
    def convertRowToRecommendation(self, row) -> Recommendation:
        user_id = row[0]
        priority = row[1]
        genre_id = row[2]
        return Recommendation(user_id, priority, genre_id)
