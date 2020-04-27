class GenerateRecommendation:

    # Parameterized Constructor
    def __init__(self, userId: int = None) -> None:
        self.userId = userId

    def getUserID(self) -> int:
        return self.userId

    def setUserID(self, userId: int) -> None:
        self.userId = userId

    def __str__(self) -> str:
        return f"User ID: {self.getUserID()}"


if __name__ == "__main__":
    print(GenerateRecommendation(1))