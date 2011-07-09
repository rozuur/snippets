class Parker:
    def __init__(self, type, role):
        self.type = type
        self._role = role

    def vehicleType(self):
        return self.type

    def role(self):
        # returns the role of parker VIP, customer, etc
        return self._role

    def park(self, parkingSpace):
        # parks the vehicle in parking space
        if parkingSpace.isEmpty() and parkingSpace.canPark(self):
            parkingSpace.setParker(self)

    def unpark(self, parkingSpace):
        # un park the vehicle
        parkingSpace.setParker(None)

class ParkingSpace:
    def __init__(self, accessibility, position):
        # initializes parking space with accessibility roles which are 
        # allowed to park
        self.roles = accessibility
        self.position = position # position from parking lot's entrance
        self.parked = False
        self.parker = None

    def isEmpty(self):
        # returns true if the space is occupied
        return self.parked

    def setParker(self, parker):
        # fills parking space with parker
        self.parker  = parker
        self.parked = True

    def getParker(self):
        # returns parker object who has occupied this space
        return self.parker

    def canOccupy(self, parker):
        # returns true if parker can occupy this position
        return parker.role() in self.roles and not self.isEmpty()

class ParkingLot:
    def __init__(self, parkingSpaces):
        # initializes all parking spaces
        self.parkingSpaces = parkingSpaces

    def _vacantSpaces(self):
        return [p.isEmpty() for p in self.parkingSpaces]

    def isFull(self):
        # returns true if no parking spaces are available to parking
        return not self.vacantSpaces.any()

    def issueTicket(self, parker):
        # issues ticket for parking
        return random.randint()

    def getVacantSpace(self):
        # returns a vacant space near to entrance
        try:
            return self._vacantSpaces()[0]
        except:
            return []

        
