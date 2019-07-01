import sys
sys.path.append('../main')
import unittest
from Robot import Robot
from ParkingLot import ParkingLot
from Car import Car
from AllParkinglotsFullException import AllParkinglotsFullException

class RobotTest(unittest.TestCase):
    def test_should_parking_in_the_first_parkingLot_when_first_parkingLot_is_not_full(self):
        robot = Robot()
        parkingLotA = ParkingLot()
        robot.addParkingLot('A', parkingLotA)
        parkingLotB = ParkingLot()
        robot.addParkingLot('B', parkingLotB)
        car = Car()
        ticket = robot.parking(car)
        assert ticket.getParkinglotNum() is 'A'

    def test_should_parking_in_the_second_parkingLot_when_first_parkingLot_is_full(self):
        robot = Robot()
        parkingLotA = ParkingLot(1)
        robot.addParkingLot('A', parkingLotA)
        parkingLotB = ParkingLot()
        robot.addParkingLot('B', parkingLotB)
        car1 = Car()
        car2 = Car()
        ticketA = robot.parking(car1)
        ticketB = robot.parking(car2)

        assert ticketA.getParkinglotNum() is 'A'
        assert ticketB.getParkinglotNum() is 'B'

    def test_should_throw_error_when_all_parkingLots_are_full(self):
        with self.assertRaises(AllParkinglotsFullException):
             robot = Robot()
             parkingLotA = ParkingLot(1)
             robot.addParkingLot('A', parkingLotA)
             car1 = Car()
             car2 = Car()
             robot.parking(car1)
             robot.parking(car2)

    def test_should_pick_car_successfully_when_ticket_is_valid(self):
        robot = Robot()
        parkingLotA = ParkingLot()
        robot.addParkingLot('A', parkingLotA)
        parkingLotB = ParkingLot()
        robot.addParkingLot('B', parkingLotB)
        car = Car()
        ticket = robot.parking(car)
        parkedCar = robot.pickCar(ticket)
        assert parkedCar is car
