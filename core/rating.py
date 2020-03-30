class Rating:

    # Parameterized Constructor
    def __init__(self, userId:int = None, movieId:int = None, rating:float = None) -> None:
        self.userId = userId
        self.movieId = movieId
        self.rating = rating

    def getUserID(self) -> int:
        return self.userId

    def getMovieID(self) -> int:
        return self.movieId

    def getRating(self) -> float:
        return self.rating

    def setUserID(self, userId:int) -> None:
        self.userId = userId

    def setMovieID(self, movieId:int) -> None:
        self.movieId = movieId

    def setRating(self, rating:float) -> None:
        self.rating = rating

    def __str__(self) -> str:
        return f"User ID: {self.getUserID()}, Movie ID: {self.getMovieID()}, Rating: {self.getRating()}"


if __name__ == "__main__":
    pass