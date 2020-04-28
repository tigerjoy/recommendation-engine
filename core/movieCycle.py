class MovieCycle:

    def __init__(self, user_id: int = None, last_movie_id: int = None, second_last_movie_id: int = None,
                 priority: int = None):
        self.user_id = user_id
        self.last_movie_id = last_movie_id
        self.second_last_movie_id = second_last_movie_id
        self.priority = priority

    def getUserID(self):
        return self.user_id

    def getLastMovieID(self):
        return self.last_movie_id

    def getSecondLastMovieID(self):
        return self.second_last_movie_id

    def getPriority(self):
        return self.priority

    def setUserID(self, user_id):
        self.user_id = user_id

    def setLastMovieID(self, last_movie_id):
        self.last_movie_id = last_movie_id

    def setSecondLastMovieID(self, second_last_movie_id):
        self.second_last_movie_id = second_last_movie_id

    def setPriority(self, priority):
        self.priority = priority

    def __str__(self):
        return (f"User ID: {self.user_id} Last Movie ID: {self.last_movie_id}\n" +
                f"Second Last Movie ID: {self.second_last_movie_id} Priority: {self.getPriority()}")


if __name__ == "__main__":
    print(MovieCycle(1, 9, 10, 3))
