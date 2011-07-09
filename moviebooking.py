class Seat:
    def __init__(self, position):
        self._position = position
        self.occupied = False
        self.classType = 'Normal'

    def getPosition(self):
        return self._position

class MovieTheatre:
    def __init__(self, seats):
        self.seats = seats
        self.movie = None

    def setMovie(self, name):
        self.movie = name

    def getMovie(self):
        return self.movie

    def setClassPriceValues(self, relations):
        # updates value of each class
        pass 

    def getClasses(self):
        # returns all the classes present in theatre, balcony, 1st class etc
        pass

    def askClassInput(self):
        # asks user for class of his choice
        print self.getClasses()
        return selectedClass

    def getSeat(self, position):
        # return the seat based on its position
        pass

    def displaySeats(self):
        pass

    def startProcess(self):
        seats = []
        # first asks user for his class choice
        clas = self.askClassInput()
        # displays all the seats available based on occupencey
        self.displaySeats()
        # appends seats selected into seats
        while not seatsSelectionCompleted:
            seat = self.getSeat(userSelectedPosition)
            seat.occupied = True # sets occupency of seat
            seats.append(seat)
        self.beginTransaction(seats, clas)
        
    def _recieveAmount(self, amount):
        # returns true if user has transferred amount
        pass
    
    def _getTotalAmount(seats, clas):
        # returns total amount based on class price relations and 
        # number of seats
        pass

    def beginTransaction(self, seats, clas):
        # begins transaction based on seats and class selected
        amount = self.getTotalAmount(seats, clas)
        recieved = self._recieveAmount(amount)
        if recieved:
            self.endTransaction()
        else:
            for s in seats:
                s.occupied = False # remove seat occupency

    def endTransaction(self):
        # ends transaction
        pass
