# elevatorsim
# @File:   building.py
# @Time:   10/08/2021
# @Author: Gabriel O.

from dataclasses import dataclass

from elevator import Elevator


@dataclass()
class Building:
    _elevator: Elevator = None
    floors: int = 18
    floorheight: float = 4.1

    @property
    def elevator(self):
        return self._elevator

    @elevator.setter
    def elevator(self, ele):
        self._elevator = ele
