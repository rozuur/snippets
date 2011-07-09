class Parker:
    def __init__(self, type, roles):
        self.type = type
        self.roles = roles

    def vehicleType(self):
        return self.type

    def role(self):
        # returns the role of parker VIP, customer, etc
        pass
    def park(self, parkingSpace):
        # parks the vehicle in parking space
        pass
    def unpark(self, parkingSpace):
        pass

class ParkingSpace:
    def __init__(self, accessibility):
        # initializes parking space with accessibility roles which are 
        # allowed to park
        pass
    def position(self, entrance):
        # returns the position of space from parking lot's entrance
        pass
    def isEmpty(self):
        # returns true if the space is occupied
        pass
    def setParker(self, parker):
        # fills parking space
        pass
    def getParker(self):
        # returns parker object who has occupied this space
        pass
    def canOccupy(self, parker):
        # returns true if parker can occupy this position
        pass

class ParkingLot:
    def __init__(self, parkingSpaces):
        # initializes all parking spaces
        pass
    def isFull(self):
        # returns true if no parking spaces are available to parking
        pass
    def issueTicket(self, parker):
        # issues ticket for parking
        pass
    def getVacantSpace(self):
        # returns a vacant space near to entrance
        pass
