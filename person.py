# elevatorsim
# @File:   person.py
# @Time:   10/08/2021
# @Author: Gabriel O.


class Person:
    def __init__(self, floor):
        self.floor = floor
        self.weekday = choice(profiles_weekdays, weights)
        self.weekend = choice(profiles_weekends, weights)