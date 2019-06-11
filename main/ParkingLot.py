from Ticket import Ticket
from CartParkedException import CartParkedException
from ParkingLotFullException import ParkingLotFullException
from InvalidTicketException import InvalidTicketException


class ParkingLot:

    def __init__(self, capacity=1):
        self.__parkedRecords = {}
        self.__capacity = capacity

    def is_park(self, car):
        if self.__is_car_parked(car):
            raise CartParkedException()
        if self.__capacity <= len(self.__parkedRecords):
            raise ParkingLotFullException()
        return self.__add_parked_record(car)

    def __add_parked_record(self, car):
        ticket = Ticket()
        self.__parkedRecords[ticket] = car
        return ticket

    def __is_car_parked(self, car):
        return car in self.__parkedRecords.values()

    def pick_car(self, ticket):
        if ticket not in self.__parkedRecords.keys():
            raise InvalidTicketException()

        return self.__parkedRecords.pop(ticket)
