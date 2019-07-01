#!/usr/bin/python
# -*- coding: UTF-8 -*-
import sys
sys.path.append('../main')
import unittest
from ParkingLot import ParkingLot
from Car import Car
from CarParkedException import CarParkedException
from ParkinglotFullException import ParkinglotFullException
from InvalidTicketException import InvalidTicketException

class ParkingLotTest(unittest.TestCase):

    def test_should_get_ticket_when_park_car(self):
        parkinglotA = ParkingLot()
        car = Car()
        ticket = parkinglotA.park(car, 'A')
        assert ticket is not None

    def test_should_throw_error_when_park_same_car_twice(self):
        with self.assertRaises(CarParkedException):
            parkinglot = ParkingLot()
            car = Car()
            parkinglot.park(car, 'A')
            parkinglot.park(car, 'A')

    def test_should_throw_error_when_park_car_in_full_parking_lot(self):
        with self.assertRaises(ParkinglotFullException):
            parkinglot = ParkingLot(1)
            car1 = Car()
            car2 = Car()
            parkinglot.park(car1, 'A')
            parkinglot.park(car2, 'A')

    def test_should_get_car_when_pick_car_with_available_ticket(self):
        parkingLot = ParkingLot()
        car = Car()
        ticket = parkingLot.park(car, 'A')
        parkedCar = parkingLot.pick(ticket)
        assert parkedCar is car

    def test_should_throw_error_when_pick_car_with_invalid_ticket(self):
        with self.assertRaises(InvalidTicketException):
            parkingLot = ParkingLot()
            ticket = None
            parkingLot.pick(ticket)

    def test_should_throw_error_when_pick_car_twice_same_ticket(self):
        with self.assertRaises(InvalidTicketException):
            parkingLot = ParkingLot()
            car = Car()
            ticket = parkingLot.park(car, 'A')
            pickedCar = parkingLot.pick(ticket)
            assert pickedCar is car
            parkingLot.pick(ticket)




