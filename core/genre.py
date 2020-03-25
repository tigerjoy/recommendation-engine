class Genre:
    def __init__(self, genreId, genreName):
        self.genreId = genreId
        self.genreName = genreName

    def getGenreID(self):
        return self.genreId

    def getGenreName(self):
        return self.genreName

    def setGenreID(self, genreId):
        self.genreId = genreId

    def setGenreName(self, genreName):
        self.genreName = genreName

    def __str__(self):
        return f"Genre ID: {self.getGenreID()}, Genre Name: {self.getGenreName()}"

if __name__ == "__main__":
    pass