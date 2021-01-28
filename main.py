import random
import heapq


class building:
    def __init__(self, floors):
        self.floors = floors
        self.floorheight = 4.1
        self

    def createElevator(self, spd = 3, acc = 1.5, jerk = 1.6, cap = 4):
        self.elevator = elevator(spd, acc, jerk, cap)

class rider:
    def __init__(self):
        self.weekday = choice(profiles_weekdays, weights)
        self.weekend = choice(profiles_weekends, weights)

class elevator:
    def __init__(self, spd, acc, jerk, cap):
        self.spd_max = spd
        self.acc_max = acc
        self.jerk_max = jerk
        self.cap = cap
        self.order_down = []
        self.order_up = []
        self.floor = 0
        self.direction = 0  # -1 down, 0 still, 1 up

    def board(self, person):
        if len(self.passengers) < self.cap:
            self.passengers.append(person)
            if person.destination > self.floor:
                heapq.heappush(order_up, person.destination)
            else:
                heapq.heappush(order_down, person.destination)
            return True
        else:
            return False

mybuilding = building(18)
mybuilding.createElevator(3, 1.5, 1.6, 4)

## main loop
