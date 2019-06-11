import unittest
import sys

sys.path.append("../main")
from ParkingLot import ParkingLot
from Car import Car
from CartParkedException import CartParkedException
from ParkingLotFullException import ParkingLotFullException
from InvalidTicketException import InvalidTicketException
from Ticket import Ticket


class ParkingLotTest(unittest.TestCase):

    def test_shoule_get_ticket_when_park_car(self):
        parking_lot = ParkingLot()
        ticket = parking_lot.is_park(Car())
        assert ticket is not None

    def test_should_throw_error_when_park_same_car_twice(self):
        with self.assertRaises(CartParkedException):
            parking_lot = ParkingLot(1)
            car = Car()
            parking_lot.is_park(car)
            parking_lot.is_park(car)

    def test_should_throw_error_when_park_car_in_full_parking_lot(self):
        with self.assertRaises(ParkingLotFullException):
            parking_lot = ParkingLot(1)
            parking_lot.is_park(Car())
            parking_lot.is_park(Car())

    def test_should_get_car_when_the_ticket_is_available(self):
        parking_lot = ParkingLot()
        car = Car()
        ticket = parking_lot.is_park(car)
        parked_car = parking_lot.pick_car(ticket)
        assert parked_car is car

    def test_should_throw_error_when_the_ticket_invalid(self):
        with self.assertRaises(InvalidTicketException):
            parking_lot = ParkingLot()
            car = Car()
            parking_lot.is_park(car)
            ticket = Ticket()
            parking_lot.pick_car(ticket)

    def test_should_throw_error_when_ticket_used_twice(self):
        with self.assertRaises(InvalidTicketException):
            parking_lot = ParkingLot()
            ticket = parking_lot.is_park(Car())
            car = parking_lot.pick_car(ticket)
            assert car is not None
            parking_lot.pick_car(ticket)
