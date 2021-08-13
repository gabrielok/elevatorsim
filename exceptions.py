# elevatorsim
# @File:   exceptions.py
# @Time:   13/08/2021
# @Author: Gabriel O.


class ValidationException(Exception):

    def __init__(self, message):
        super().__init__(message)


class BadPhysicsException(ValidationException):

    def __init__(self):
        message = (f"Choose a duration for the simulation by attributing at least"
                   f" one of the parameters: hours, days or weeks")
        super().__init__(message)
