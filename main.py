import random



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
        self.count = 0
        self.passengers = []

    def board(self, person):
        if len(self.passengers) < self.cap:
            self.passengers.append(person)
            return True
        else:
            return False

mybuilding = building(18)
mybuilding.createElevator(3, 1.5, 1.6, 4)
## main loop
