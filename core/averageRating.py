class AverageRating:

    # Non-Parameterized Constructor
    def __init__(self):
        self.movieId = None
        self.avgRating = None

    # Parameterized Constructor
    def __init__(self, movieId:int, avgRating:float) -> None:
        self.movieId = movieId
        self.avgRating = avgRating

    def getMovieID(self) -> int:
        return self.movieId

    def getAverageRating(self) -> float:
        return self.avgRating

    def setMovieID(self, movieId:int) -> None:
        self.movieId = movieId

    def setAverageRating(self, avgRating:float) -> None:
        self.avgRating = avgRating

    def __str__(self) -> str:
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
