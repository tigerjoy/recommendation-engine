class Movie:

    # Parameterized Constructor
    def __init__(self, movieId:int = None, title:str = None, genres:str = None) -> None:
        self.movieId = movieId
        self.title = title
        self.genres = genres

    def getMovieID(self) -> int:
        return self.movieId

    def getTitle(self) -> str:
        return self.title

    def getGenres(self) -> str:
        return self.genres

    def setMovieID(self, movieId:int) -> None:
        self.movieId = movieId

    def setTitle(self, title:str) -> None:
        self.title = title

    def setGenres(self, genres:str) -> None:
        self.genres = genres

    def __str__(self) -> str:
        return f"Movie ID: {self.getMovieID()}, Title: {self.getTitle()}, Genres: {self.getGenres()}"


if __name__ == "__main__":
    pass