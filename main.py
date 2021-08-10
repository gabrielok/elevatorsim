# elevatorsim
# @File:   main.py
# @Time:   10/08/2021
# @Author: Gabriel O.

from building import Building
from elevator import Elevator

mybuilding = Building(floors=18,
                      floorheight=4.1)
mybuilding.elevator = Elevator()

