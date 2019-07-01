from AllParkinglotsFullException import AllParkinglotsFullException
from InvalidTicketException import InvalidTicketException

class Robot:
    def __init__(self):
        self.__parkingLots = {}

    def addParkingLot(self, number, parkingLot):
        self.__parkingLots[number] = parkingLot

    def parking(self, car):
        ticket = {}
        for parkingLotNum, parkingLot in self.__parkingLots.items():
            if not parkingLot.isParkingLotFulled():
                ticket = parkingLot.park(car, parkingLotNum)
                break
        if not ticket:
            raise AllParkinglotsFullException
        return ticket

    def pickCar(self, ticket):
        parkingLotNum = ticket.getParkinglotNum()
        if not self.__parkingLots[parkingLotNum]:
            raise InvalidTicketException
        return self.__parkingLots[parkingLotNum].pick(ticket)