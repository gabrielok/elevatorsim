# elevatorsim
# @File:   elevator.py
# @Time:   10/08/2021
# @Author: Gabriel O.

import heapq


class Elevator:
    def __init__(self, spd = 3, acc = 1.5, jerk = 1.6, cap = 4):
        self.spd_max = spd
        self.acc_max = acc
        self.jerk_max = jerk
        self.cap = cap
        self.count = 0
        self.order_down = []
        self.order_up = []
        self.floor = 0
        self.direction = 0  # -1 down, 0 still, 1 up

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
                self.direction = 1
            elif len(self.order_down) > 0:
                self.direction = -1

    def peek(self):
        if self.direction == 1:
            return self.order_up[0]
        elif self.direction == -1:
            return - self.order_down[0]

    def board(self, person):
        if self.count < self.cap:
            self.push(person.destination)
            self.count = self.count + 1
            return True
        else:
            return False

    def disembark(self):
        self.count = self.count - 1
        if self.direction == -1:
            heapq.heappop(self.order_down)
            if len(self.order_down) == 0:    # reached final down destination
                if len(self.order_up) > 0:   # if there are up destinations in queue
                    self.direction = 1
                else:                   # there are no destinations in queue
                    self.direction = 0
        else:
            heapq.heappop(self.order_up)
            if len(self.order_up) == 0:    # reached final up destination
                if len(self.order_down) > 0:   # if there are down destinations in queue
                    self.direction = -1
                else:                   # there are no destinations in queue
                    self.direction = 0
