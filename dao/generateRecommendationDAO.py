from core.generateRecommendation import GenerateRecommendation
from typing import List
import sqlite3
import json


class GenerateRecommendationDAO():

    # Constructor
    def __init__(self, prop_file: str) -> None:
        self.prop_file = prop_file
        # Get DB properties
        with open(prop_file, "r") as prop:
            content = json.loads(prop.read())
            dbURL = content["GenerateRecommendation"]["dbURL"]
            self.tableName = content["GenerateRecommendation"]["tableName"]
        # Connect to the database
        self.myConn = sqlite3.connect(dbURL)

        # print(f"DB connection successful to {dbURL}")

    # Destructor
    def __del__(self) -> None:
        self.myConn.close()

    # Returns the user_ids for whom the generation of recommendation
    # are either processing or left
    def getAllUserID(self) -> List[GenerateRecommendation]:
        output = []
        cursor = self.myConn.execute(f"SELECT * FROM {self.tableName}")
        for row in cursor:
            output.append(self.convertRowToGenerateRecommendation(row))
        return output

    # Adds the user_id to the table
    def addUserID(self, the_user: GenerateRecommendation) -> bool:
        query = f"""
                    INSERT INTO '{self.tableName}'('userId') 
                    VALUES (?);
                """

        data_tuple = (the_user.getUserID(), )

        self.myConn.execute(query, data_tuple)

        self.myConn.commit()

        return self.myConn.total_changes > 0

    # Deletes the user_id from the table
    def deleteUserID(self, the_user: GenerateRecommendation) -> bool:
        query = f"""
                    DELETE FROM {self.tableName}
                    WHERE userId = {the_user.getUserID()}
                """
        self.myConn.execute(query)
        self.myConn.commit()
        return self.myConn.total_changes > 0

    # Searches for a user_id from the table
    def searchByUserID(self, the_user: GenerateRecommendation) -> List[GenerateRecommendation]:
        output = []
        query = f"""
                    SELECT *
                    FROM {self.tableName}
                    WHERE userId = {the_user.getUserID()}
                """
        cursor = self.myConn.execute(query)
        for row in cursor:
            output.append(self.convertRowToGenerateRecommendation(row))
        return output

    def convertRowToGenerateRecommendation(self, row):
        user_id = row[0]
        return GenerateRecommendation(user_id)
