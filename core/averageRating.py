class AverageRating:

    # Constructor
    def __init__(self, movieId, avgRating):
        self.movieId = movieId
        self.avgRating = avgRating

    def getMovieID(self):
        return self.movieId

    def getAverageRating(self):
        return self.avgRating

    def setMovieID(self, movieId):
        self.movieId = movieId

    def setAverageRating(self, avgRating):
        self.avgRating = avgRating

    def __str__(self):
        return f"Movie ID: {self.getMovieID()}, Average Rating: {self.getAverageRating()}"

if __name__ == "__main__":
    obj = AverageRating(1, 3.4)

    print('obj.getMovieID() = ', obj.getMovieID())
    print('obj.getAverageRating() = ', obj.getAverageRating())
    print(obj)

    obj.setMovieID(3)
    obj.setAverageRating(4)

    print('obj.getMovieID() = ', obj.getMovieID())
    print('obj.getAverageRating() = ', obj.getAverageRating())

    print(obj)
