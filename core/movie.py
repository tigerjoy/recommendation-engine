class Movie:
    def __init__(self, movieId, title, genres):
        self.movieId = movieId
        self.title = title
        self.genres = genres

    def getMovieID(self):
        return self.movieId

    def getTitle(self):
        return self.title

    def getGenres(self):
        return self.genres

    def setMovieID(self, movieId):
        self.movieId = movieId

    def setTitle(self, title):
        self.title = title

    def setGenres(self, genres):
        self.genres = genres

    def __str__(self):
        return f"Movie ID: {self.getMovieID()}, Title: {self.getTitle()}, Genres: {self.getGenres()}"

if __name__ == "__main__":
    pass