class MovieGenre:

    # Non-Parameterized Constructor
    def __init__(self):
        self.movieId = None
        self.genreId = None

    # Parameterized Constructor
    def __init__(self, movieId:int, genreId:int) -> None:
        self.movieId = movieId
        self.genreId = genreId

    def getGenreID(self) -> int:
        return self.genreId

    def getMovieID(self) -> int:
        return self.movieId

    def setGenreID(self, genreId:int) -> None:
        self.genreId = genreId

    def setMovieID(self, movieId:int) -> None:
        self.movieId = movieId

    def __str__(self) -> str:
        return f"Genre ID: {self.getGenreID()}, Movie ID: {self.getMovieID()}"


if __name__ == "__main__":
    pass