class MovieCycle:

    def __init__(self, user_id: int = None, last_movie_id: int = None, second_last_movie_id: int = None):
        self.user_id = user_id
        self.last_movie_id = last_movie_id
        self.second_last_movie_id = second_last_movie_id

    def getUserID(self):
        return self.user_id

    def getLastMovieID(self):
        return self.last_movie_id

    def getSecondLastMovieID(self):
        return self.second_last_movie_id

    def setUserID(self, user_id):
        self.user_id = user_id

    def setLastMovieID(self, last_movie_id):
        self.last_movie_id = last_movie_id

    def setSecondLastMovieID(self, second_last_movie_id):
        self.second_last_movie_id = second_last_movie_id

    def __str__(self):
        return f"User ID: {self.user_id} Last Movie ID: {self.last_movie_id} Second Last Movie ID: {self.second_last_movie_id}"

if __name__ == "__main__":
    print(MovieCycle(1, 9, 10))