class MovieGenre:
    def __init__(self, movieId, genreId):
        self.movieId = movieId
        self.genreId = genreId

    def getGenreID(self):
        return self.genreId

    def getMovieID(self):
        return self.movieId

    def setGenreID(self, genreId):
        self.genreId = genreId

    def setMovieID(self, movieId):
        self.movieId = movieId

    def __str__(self):
        return f"Genre ID: {self.getGenreID()}, Movie ID: {self.getMovieID()}"

if __name__ == "__main__":
    pass