import json
import sqlite3
from typing import List
from core.tempRecommendation import TempRecommendation


class TempRecommendationDAO():

    # Constructor
    def __init__(self, prop_file: str) -> None:
        self.prop_file = prop_file
        # Get DB properties
        with open(prop_file, "r") as prop:
            content = json.loads(prop.read())
            dbURL = content["TempRecommendation"]["dbURL"]
            self.tableName = content["TempRecommendation"]["tableName"]
        # Connect to the database
        self.myConn = sqlite3.connect(dbURL)

        # print(f"DB connection successfull to {dbURL}")

    # Destructor
    def __del__(self) -> None:
        self.myConn.close()

    # Return a list of Recommendation objects
    # containing all the rows present in the recommendation table
    def getAllTempRecommendation(self) -> List[TempRecommendation]:
        output = []
        cursor = self.myConn.execute(f"SELECT * FROM {self.tableName}")
        for row in cursor:
            output.append(self.convertRowToTempRecommendation(row))
        return output

    def getTempRecommendationByUserID(self, user_id: int) -> List[TempRecommendation]:
        output = []
        query = f"""
                    SELECT * 
                    FROM {self.tableName}
                    WHERE user_id = {user_id}
                """
        cursor = self.myConn.execute(query)
        for row in cursor:
            output.append(self.convertRowToTempRecommendation(row))
        return output

    def addTempRecommendation(self, the_temp_recommendation: TempRecommendation) -> bool:
        query = f"""
                    INSERT INTO '{self.table_name}'('user_id', 'last_combination', 'priority', 'combination_num', 
                                                     'common_movie_length', 'genres') 
                    VALUES (?, ?, ?, ?, ?, ?);
                """

        data_tuple = (the_temp_recommendation.getUserID(), the_temp_recommendation.getLastCombination(),
                      the_temp_recommendation.getPriority(), the_temp_recommendation.getCombinationNum(),
                      the_temp_recommendation.getCommonMovieLength(), the_temp_recommendation.getGenres())

        self.myConn.execute(query, data_tuple)

        self.myConn.commit()

        return self.myConn.total_changes > 0

    def deleteTempRecommendation(self, the_temp_recommendation: TempRecommendation) -> bool:
        query = f"""
                    DELETE FROM {self.tableName}
                    WHERE user_id = {the_temp_recommendation.getUserID()}
                """
        self.my_conn.execute(query)

        self.my_conn.commit()

        return self.myConn.total_changes > 0

    # Return a Rating object by converting
    # a row list of SQLite to Rating(userId, movieId, rating)
    def convertRowToTempRecommendation(self, row) -> TempRecommendation:
        user_id = row[0]
        last_combination = row[1]
        priority = row[2]
        combination_num = row[3]
        common_movie_length = row[4]
        genres = row[5]

        return TempRecommendation(user_id, last_combination, priority, combination_num, common_movie_length, genres)
