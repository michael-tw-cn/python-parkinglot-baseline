from CarParkedException import CarParkedException
from ParkinglotFullException import ParkinglotFullException
from InvalidTicketException import InvalidTicketException
from Ticket import Ticket

class ParkingLot:
    def __init__(self, capacity=10):
        self.__parkedRecords = {}
        self.__capacity = capacity

    def park(self, car, parkingLotNum):
        if self.__isCarParked(car):
            raise CarParkedException()
        self.__addParkedRecord(car, parkingLotNum)
        return self.__ticket

    def __isCarParked(self, car):
        return car in self.__parkedRecords.values()

    def __addParkedRecord(self, car, parkingLotNum):
        if self.isParkingLotFulled():
            raise ParkinglotFullException
        self.__ticket = Ticket(parkingLotNum)
        self.__parkedRecords[self.__ticket] =car

    def isParkingLotFulled(self):
        return len(self.__parkedRecords) == self.__capacity

    def pick(self, ticket):
        if self.__isTicketInvalid(ticket):
            raise InvalidTicketException
        car = self.__parkedRecords[ticket]
        self.__parkedRecords.pop(ticket)
        return car

    def __isTicketInvalid(self, ticket):
        return ticket not in self.__parkedRecords.keys()