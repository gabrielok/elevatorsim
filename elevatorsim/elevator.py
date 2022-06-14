# elevatorsim
# @File:   elevator.py
# @Time:   10/08/2021
# @Author: Gabriel O.

import heapq
from dataclasses import dataclass, field
from enum import Enum, auto

from typing import List


class Direction(Enum):
    UP = auto()
    DOWN = auto()
    STILL = auto()


@dataclass
class Elevator:
    """
    High level description of an elevator, including mechanical properties, queue
    and passager status.
    """

    max_speed: float = 3
    max_acceleration: float = 1.5
    max_jerk: float = 1.6
    capacity: int = 4
    passenger_count: int = field(default=0, init=False)
    order_up: List[int] = field(default_factory=list, init=False)
    order_down: List[int] = field(default_factory=list, init=False)
    floor: int = field(default=0, init=False)
    direction: Direction = field(default=Direction.STILL, init=False)

    def push(self, destination):
        """
        Push a destination into the queue.
        :param destination: floor to go to
        :return:
        """
        if destination > self.floor:
            if destination not in self.order_up:
                heapq.heappush(self.order_up, destination)
        elif destination < self.floor:
            if destination not in self.order_down:
                # negative values for a max heap
                heapq.heappush(self.order_down, -destination)
        else:
            raise ValueError()

        if self.direction == Direction.STILL:
            if len(self.order_up) > 0:
                self.direction = Direction.UP
            elif len(self.order_down) > 0:
                self.direction = Direction.DOWN

    def peek(self) -> int:
        """
        Returns the next stop
        :return: floor where elevator is headed
        """
        if self.direction == Direction.UP:
            return self.order_up[0]
        elif self.direction == Direction.DOWN:
            return -self.order_down[0]

    def board(self, person) -> bool:
        """
        If the person can board without exceeding the elevator's passenger capacity,
        returns True and increases the elevator's passenger count
        :param person:
        :return:
        """
        if self.passenger_count < self.capacity:
            self.push(person.destination)
            self.passenger_count = self.passenger_count + 1
            return True
        else:
            return False

    def disembark(self):
        """
        Decreases the passenger count and updates the direction to still
        if there are no more passengers
        :return:
        """
        self.passenger_count = self.passenger_count - 1
        if self.direction == Direction.DOWN:
            heapq.heappop(self.order_down)
            if len(self.order_down) == 0:  # reached final down destination
                if len(self.order_up) > 0:  # if there are up destinations in queue
                    self.direction = Direction.UP
                else:  # there are no destinations in queue
                    self.direction = Direction.STILL
        else:
            heapq.heappop(self.order_up)
            if len(self.order_up) == 0:  # reached final up destination
                if len(self.order_down) > 0:  # if there are down destinations in queue
                    self.direction = Direction.DOWN
                else:  # there are no destinations in queue
                    self.direction = Direction.STILL
