class Rating:
    def __init__(self, userId, movieId, rating):
        self.userId = userId
        self.movieId = movieId
        self.rating = rating

    def getUserID(self):
        return self.userId

    def getMovieID(self):
        return self.movieId

    def getRating(self):
        return self.rating

    def setUserID(self, userId):
        self.userId = userId

    def setMovieID(self, movieId):
        self.movieId = movieId

    def setRating(self, rating):
        self.rating = rating

    def __str__(self):
        return f"User ID: {self.getUserID()}, Movie ID: {self.getMovieID()}, Rating: {self.getRating()}"

if __name__ == "__main__":
    pass