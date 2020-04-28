class UserMovieCount:

    # Parameterized Constructor
    def __init__(self, userId:int, Action:int = 0, Adventure:int = 0, Animation:int = 0,
                 Children:int = 0, Comedy:int = 0, Crime:int = 0, Documentary:int = 0, Drama:int = 0,
                 Fantasy:int = 0, FilmNoir:int = 0, Horror:int = 0, IMAX:int = 0, Musical:int = 0,
                 Mystery:int = 0,Romance:int = 0, SciFi:int = 0, Thriller:int = 0, War:int = 0,
                 Western:int = 0):
        self.userId = userId
        self.Action = Action
        self.Adventure = Adventure
        self.Animation = Animation
        self.Children = Children
        self.Comedy = Comedy
        self.Crime = Crime
        self.Documentary = Documentary
        self.Drama = Drama
        self.Fantasy = Fantasy
        self.FilmNoir = FilmNoir
        self.Horror = Horror
        self.IMAX = IMAX
        self.Musical = Musical
        self.Mystery = Mystery
        self.Romance = Romance
        self.SciFi = SciFi
        self.Thriller = Thriller
        self.War = War
        self.Western = Western
        self.genreCounts = [
            self.Action, self.Adventure, self.Animation, self.Children, self.Comedy, self.Crime, self.Documentary,
            self.Drama, self.Fantasy, self.FilmNoir, self.Horror, self.IMAX, self.Musical, self.Mystery,
            self.Romance, self.SciFi, self.Thriller, self.War, self.Western
        ]

    def getGenreCount(self):
        return self.genreCounts

    def getUserID(self) -> int:
        return self.userId

    def getActionCount(self) -> int:
        return self.Action

    def getAdventureCount(self) -> int:
        return self.Adventure

    def getAnimationCount(self) -> int:
        return self.Animation

    def getChildrenCount(self) -> int:
        return self.Children

    def getComedyCount(self) -> int:
        return self.Comedy

    def getCrimeCount(self) -> int:
        return self.Crime

    def getDocumentaryCount(self) -> int:
        return self.Documentary

    def getDramaCount(self) -> int:
        return self.Drama

    def getFantasyCount(self) -> int:
        return self.Fantasy

    def getFilmNoirCount(self) -> int:
        return self.FilmNoir

    def getHorrorCount(self) -> int:
        return self.Horror

    def getIMAXCount(self) -> int:
        return self.IMAX

    def getMusicalCount(self) -> int:
        return self.Musical

    def getMysteryCount(self) -> int:
        return self.Mystery

    def getRomanceCount(self) -> int:
        return self.Romance

    def getSciFiCount(self) -> int:
        return self.SciFi

    def getThrillerCount(self) -> int:
        return self.Thriller

    def getWarCount(self) -> int:
        return self.War

    def getWesternCount(self) -> int:
        return self.Western

    def setUserID(self, userId:int) -> None:
        self.userId = userId

    def setActionCount(self, Action:int) -> None:
        self.Action = Action

    def setAdventureCount(self, Adventure:int) -> None:
        self.Adventure = Adventure

    def setAnimationCount(self, Animation:int) -> None:
        self.Animation = Animation

    def setChildrenCount(self, Children:int) -> None:
        self.Children = Children

    def setComedyCount(self, Comedy:int) -> None:
        self.Comedy = Comedy

    def setCrimeCount(self, Crime:int) -> None:
        self.Crime = Crime

    def setDocumentaryCount(self, Documentary:int) -> None:
        self.Documentary = Documentary

    def setDramaCount(self, Drama:int) -> None:
        self.Drama = Drama

    def setFantasyCount(self, Fantasy:int) -> None:
        self.Fantasy = Fantasy

    def setFilmNoirCount(self, FilmNoir:int) -> None:
        self.FilmNoir = FilmNoir

    def setHorrorCount(self, Horror:int) -> None:
        self.Horror = Horror

    def setIMAXCount(self, IMAX:int) -> None:
        self.IMAX = IMAX

    def setMusicalCount(self, Musical:int) -> None:
        self.Musical = Musical

    def setMysteryCount(self, Mystery:int) -> None:
        self.Mystery = Mystery

    def setRomanceCount(self, Romance:int) -> None:
        self.Romance = Romance

    def setSciFiCount(self, SciFi:int) -> None:
        self.SciFi = SciFi

    def setThrillerCount(self, Thriller:int) -> None:
        self.Thriller = Thriller

    def setWarCount(self, War:int) -> None:
        self.War = War

    def setWesternCount(self, Western:int) -> None:
        self.Western = Western

    def __str__(self) -> str:
        return  'User ID: {}'.format(self.getUserID()) + \
                '\nAction: {}'.format(self.getActionCount()) + \
                '\nAdventure: {}'.format(self.getAdventureCount()) + \
                '\nAnimation: {}'.format(self.getAnimationCount()) + \
                '\nChildren: {}'.format(self.getChildrenCount()) + \
                '\nComedy: {}'.format(self.getComedyCount()) + \
                '\nCrime: {}'.format(self.getCrimeCount()) + \
                '\nDocumentary: {}'.format(self.getDocumentaryCount()) + \
                '\nDrama: {}'.format(self.getDramaCount()) + \
                '\nFantasy: {}'.format(self.getFantasyCount()) + \
                '\nFilm-Noir: {}'.format(self.getFilmNoirCount()) + \
                '\nHorror: {}'.format(self.getHorrorCount()) + \
                '\nIMAX: {}'.format(self.getIMAXCount()) + \
                '\nMusical: {}'.format(self.getMusicalCount()) + \
                '\nMystery: {}'.format(self.getMysteryCount()) + \
                '\nRomance: {}'.format(self.getRomanceCount()) + \
                '\nSci-Fi: {}'.format(self.getSciFiCount()) + \
                '\nThriller: {}'.format(self.getThrillerCount()) + \
                '\nWar: {}'.format(self.getWarCount()) + \
                '\nWestern: {}'.format(self.getWesternCount())


if __name__ == "__main__":
    pass