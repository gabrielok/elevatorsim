# elevatorsim
# @File:   main.py
# @Time:   10/08/2021
# @Author: Gabriel O.

from building import Building
from elevator import Elevator
from physics2 import Physics


def main():
    mybuilding = Building(floors=18,
                          floorheight=4.1)
    mybuilding.elevator = Elevator()
    print(mybuilding.elevator)
    mybuilding.populate()
    phys = Physics(building=mybuilding, hours=10)
    print(phys.building.elevator)


if __name__ == '__main__':
    main()
