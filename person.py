# elevatorsim
# @File:   person.py
# @Time:   10/08/2021
# @Author: Gabriel O.

from dataclasses import dataclass


@dataclass
class Person:
    floor: int


class Teen(Person):
    pass
