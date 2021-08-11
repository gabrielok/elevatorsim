# elevatorsim
# @File:   building.py
# @Time:   10/08/2021
# @Author: Gabriel O.
from abc import abstractmethod
from dataclasses import dataclass

from elevator import Elevator
from person import Person


class BuildingProfile:

    @abstractmethod
    def teenagers(self) -> float:
        # younger than 18
        pass

    @abstractmethod
    def young_adults(self) -> float:
        # between 18 and 25 years old
        pass

    @abstractmethod
    def adults(self) -> float:
        # between 25 and 45 years old
        pass

    @abstractmethod
    def older_adults(self) -> float:
        # between 45 and 65 years old
        pass

    @abstractmethod
    def elderly(self) -> float:
        # older than 65
        pass


class StandardProfile(BuildingProfile):
    teenagers = 0.2
    young_adults = 0.2
    adults = 0.3
    older_adults = 0.2
    elderly = 0.1


class YoungProfile(BuildingProfile):
    pass


class OlderProfile(BuildingProfile):
    pass


@dataclass()
class Building:
    _elevator: Elevator = None
    floors: int = 18
    floorheight: float = 4.1
    apartments_per_floor: int = 2
    residents_per_apartment: int = 2

    @property
    def elevator(self):
        return self._elevator

    @elevator.setter
    def elevator(self, ele):
        self._elevator = ele

    def populate(self, profile=StandardProfile()):
        resident_count = self.floors * self.apartments_per_floor * self.residents_per_apartment
        print(profile.teenagers, resident_count)
