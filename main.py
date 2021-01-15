import random



class building:
    # buildings contain a number of floors, an elevator and elevator users (riders)
    def __init__(self, floors):
        self.floors = floors
        self.floorheight = 4
        

class rider:
    def __init__(self):
        self.weekday = choice(profiles_weekdays, weights)
        self.weekend = choice(profiles_weekends, weights)
