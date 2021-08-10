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
    max_speed: float = 3
    max_acc: float = 1.5
    max_jerk: float = 1.6
    capacity: int = 4
    passenger_count: int = field(default=0,
                                 init=False)
    order_up: List[int] = field(default_factory=list,
                                init=False)
    order_down: List[int] = field(default_factory=list,
                                  init=False)
    floor: int = field(default=0,
                       init=False)
    direction: Direction = field(default=Direction.STILL,
                                 init=False)

    def push(self, destination):
        if destination > self.floor:
            try:
                self.order_up.index(destination)
            except ValueError:
                # destination is not yet in the heaps
                heapq.heappush(self.order_up, destination)
        else:
            try:
                self.order_down.index(- destination)
            except ValueError:
                # destination is not yet in the heaps
                heapq.heappush(self.order_down, - destination)  # negative values for a max heap

        if self.direction == 0:
            if len(self.order_up) > 0:
                self.direction = Direction.UP
            elif len(self.order_down) > 0:
                self.direction = Direction.DOWN

    def peek(self):
        if self.direction == 1:
            return self.order_up[0]
        elif self.direction == -1:
            return - self.order_down[0]

    def board(self, person):
        if self.passenger_count < self.capacity:
            self.push(person.destination)
            self.passenger_count = self.passenger_count + 1
            return True
        else:
            return False

    def disembark(self):
        self.passenger_count = self.passenger_count - 1
        if self.direction == -1:
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
