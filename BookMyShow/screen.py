class Screen:
    def __init__(self, screenId=0, seats=None):
        self.screenId = screenId
        self.seats = seats if seats else []
    
    def getScreenId(self):
        return self.screenId
    
    def setScreenId(self, screenId):
        self.screenId = screenId
    
    def getSeats(self):
        return self.seats
    
    def setSeats(self, seats):
        self.seats = seats
