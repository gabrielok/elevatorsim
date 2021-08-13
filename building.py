# elevatorsim
# @File:   building.py
# @Time:   10/08/2021
# @Author: Gabriel O.

from dataclasses import dataclass, field

from elevator import Elevator
from buildingprofile import StandardProfile


@dataclass
class Building:
    """
    High level description of a building, which has some physical parameters (number of
    floors, floor height, etc.) and an elevator.
    """
    elevator: Elevator
    _elevator: Elevator = field(init=False, repr=False)
    floors: int = 18
    floorheight: float = 4.1
    apartments_per_floor: int = 2
    residents_per_apartment: int = 2

    @property
    def elevator(self):
        return self._elevator

    @elevator.setter
    def elevator(self, e: Elevator):
        self._elevator = e

    def populate(self, profile=StandardProfile):
        resident_count = self.floors * self.apartments_per_floor * self.residents_per_apartment
        print(profile.teens, resident_count)
