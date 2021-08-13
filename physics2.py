# elevatorsim
# @File:   physics2.py
# @Time:   10/08/2021
# @Author: Gabriel O.

from dataclasses import dataclass, field

from building import Building
from elevator import Elevator
from exceptions import BadPhysicsException
from personprofile import Day


@dataclass()
class Physics:
    """
    Class used to simulate the elevator movement over the specified duration
    """
    building: Building
    starting_day: Day = Day.MONDAY
    hours: int = 0
    days: int = 0
    weeks: int = 0

    def __post_init__(self):
        _sum = self.hours + self.days + self.weeks
        if sum == 0:
            raise BadPhysicsException()

    def run(self):
        """
        Run the simulation.
        :return:
        """
        pass
