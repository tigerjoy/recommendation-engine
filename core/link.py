class Link:

    # Parameterized Constructor
    def __init__(self, movieId: int = None, imdbIb: int = None, tmdbIb: int = None) -> None:
        self.movieId = movieId
        self.imdbIb = imdbIb
        self.tmdbIb = tmdbIb

    def getMovieID(self) -> int:
        return self.movieId

    def getIMDBID(self) -> str:
        return self.imdbIb

    def getTMDBID(self) -> str:
        return self.tmdbIb

    def setMovieID(self, movieId: int) -> None:
        self.movieId = movieId

    def setIMDBID(self, imdbIb: int) -> None:
        self.imdbIb = imdbIb

    def setTMDBID(self, tmdbIb: int) -> None:
        self.tmdbIb = tmdbIb

    def __str__(self) -> str:
        return f"Movie ID: {self.getMovieID()}, IMDB ID: {self.getIMDBID()} TMDB ID: {self.getTMDBID()}"


if __name__ == "__main__":
    print(Link(1, 3, 5))