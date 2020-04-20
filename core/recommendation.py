class Recommendation:

    # Parameterized Constructor
    def __init__(self, user_id:int = None, priority:int = None, genre_id:int = None) -> None:
        self.user_id = user_id
        self.priority = priority
        self.genre_id = genre_id

    def getUserID(self):
        return self.user_id

    def getPriority(self):
        return self.priority

    def getGenreID(self):
        return self.genre_id

    def setUserID(self, user_id):
        self.user_id = user_id

    def setPriority(self, priority):
        self.priority = priority

    def setGenreID(self, genre_id):
        self.genre_id = genre_id

    def __str__(self) -> str:
        return f"User ID: {self.getUserID()}, Priority: {self.getPriority()}, GenreID: {self.getGenreID()}"


if __name__ == "__main__":
    obj = Recommendation(1, 1, 3)
    print(obj)