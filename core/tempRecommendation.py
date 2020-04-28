class TempRecommendation:

    # Parameterized Constructor
    def __init__(self, user_id: int = None, last_combination: int = None, priority: int = None,
                 combination_num: int = None, common_movie_length: int = None, genres: str = None) -> None:
        self.user_id = user_id
        self.last_combination = last_combination
        self.priority = priority
        self.combination_num = combination_num
        self.common_movie_length = common_movie_length
        self.genres = genres

    def getUserID(self):
        return self.user_id

    def getLastCombination(self):
        return self.last_combination

    def getPriority(self):
        return self.priority

    def getCombinationNum(self):
        return self.combination_num

    def getCommonMovieLength(self):
        return self.common_movie_length

    def getGenres(self):
        return self.genres

    def setUserID(self, user_id):
        self.user_id = user_id

    def setLastCombination(self, last_combination):
        self.last_combination = last_combination

    def setPriority(self, priority):
        self.priority = priority

    def setCombinationNum(self, combination_num):
        self.combination_num = combination_num

    def setCommonMovieLength(self, common_movie_length):
        self.common_movie_length = common_movie_length

    def setGenres(self, genres):
        self.genres = genres

    def __str__(self) -> str:
        return (f"User ID: {self.getUserID()}, \n" +
                f"Last Combination: {self.getLastCombination()}, Priority: {self.getPriority()}, \n" +
                f"Combination Num: {self.getCombinationNum()}, Common Movie Length: {self.getcommonMovieLength()}\n" +
                f"Genres: {self.getGenres()}")


if __name__ == "__main__":
    obj = TempRecommendation(1, 1, 3, 56, 11, "5, 6, 7")
    print(obj)
