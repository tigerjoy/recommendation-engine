class UserMovieCount:
    def __init__(self, userId, Action, Adventure, Animation, Children, Comedy, Crime, Documentary, Drama, Fantasy, FilmNoir, Horror, IMAX, Musical, Mystery, Romance, SciFi, Thriller, War, Western):
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

    def getUserID(self):
        return self.userId

    def getActionCount(self):
        return self.Action

    def getAdventureCount(self):
        return self.Adventure

    def getAnimationCount(self):
        return self.Animation

    def getChildrenCount(self):
        return self.Children

    def getComedyCount(self):
        return self.Comedy

    def getCrimeCount(self):
        return self.Crime

    def getDocumentaryCount(self):
        return self.Documentary

    def getDramaCount(self):
        return self.Drama

    def getFantasyCount(self):
        return self.Fantasy

    def getFilmNoirCount(self):
        return self.FilmNoir

    def getHorrorCount(self):
        return self.Horror

    def getIMAXCount(self):
        return self.IMAX

    def getMusicalCount(self):
        return self.Musical

    def getMysteryCount(self):
        return self.Mystery

    def getRomanceCount(self):
        return self.Romance

    def getSciFiCount(self):
        return self.SciFi

    def getThrillerCount(self):
        return self.Thriller

    def getWarCount(self):
        return self.War

    def getWesternCount(self):
        return self.Western

    def setUserID(self, userId):
        self.userId = userId

    def setActionCount(self, Action):
        self.Action = Action

    def setAdventureCount(self, Adventure):
        self.Adventure = Adventure

    def setAnimationCount(self, Animation):
        self.Animation = Animation

    def setChildrenCount(self, Children):
        self.Children = Children

    def setComedyCount(self, Comedy):
        self.Comedy = Comedy

    def setCrimeCount(self, Crime):
        self.Crime = Crime

    def setDocumentaryCount(self, Documentary):
        self.Documentary = Documentary

    def setDramaCount(self, Drama):
        self.Drama = Drama

    def setFantasyCount(self, Fantasy):
        self.Fantasy = Fantasy

    def setFilmNoirCount(self, FilmNoir):
        self.FilmNoir = FilmNoir

    def setHorrorCount(self, Horror):
        self.Horror = Horror

    def setIMAXCount(self, IMAX):
        self.IMAX = IMAX

    def setMusicalCount(self, Musical):
        self.Musical = Musical

    def setMysteryCount(self, Mystery):
        self.Mystery = Mystery

    def setRomanceCount(self, Romance):
        self.Romance = Romance

    def setSciFiCount(self, SciFi):
        self.SciFi = SciFi

    def setThrillerCount(self, Thriller):
        self.Thriller = Thriller

    def setWarCount(self, War):
        self.War = War

    def setWesternCount(self, Western):
        self.Western = Western

    def __str__(self):
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