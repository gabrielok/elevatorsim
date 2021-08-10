# elevatorsim
# @File:   building.py
# @Time:   10/08/2021
# @Author: Gabriel O.


class Building:
    def __init__(self, floors = 18):
        self.floors = floors
        self.floorheight = 4.1

    def createElevator(self, spd, acc, jerk, cap):
        self.elevator = elevator(spd, acc, jerk, cap)