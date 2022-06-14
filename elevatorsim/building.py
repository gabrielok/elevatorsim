# elevatorsim
# @File:   building.py
# @Time:   10/08/2021
# @Author: Gabriel O.

from dataclasses import dataclass

from .elevator import Elevator
from .buildingprofile import BuildingProfile


@dataclass
class Building:
    """
    High level description of a building, which has some physical parameters (number of
    floors, floor height, etc.), an elevator and residents.
    """

    elevator: Elevator
    profile: BuildingProfile
    floors: int = 18
    floor_height: float = 4.1
    apartments_per_floor: int = 2
    residents_per_apartment: int = 2

    def __post_init__(self):
        resident_count = (
            self.floors * self.apartments_per_floor * self.residents_per_apartment
        )
