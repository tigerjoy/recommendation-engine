class Genre:

    # Parameterized Constructor
    def __init__(self, genreId:int = None, genreName:str = None) -> None:
        self.genreId = genreId
        self.genreName = genreName

    def getGenreID(self) -> int:
        return self.genreId

    def getGenreName(self) -> str:
        return self.genreName

    def setGenreID(self, genreId:int) -> None:
        self.genreId = genreId

    def setGenreName(self, genreName:str) -> None:
        self.genreName = genreName

    def __str__(self) -> str:
        return f"Genre ID: {self.getGenreID()}, Genre Name: {self.getGenreName()}"


if __name__ == "__main__":
    pass