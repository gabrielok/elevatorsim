# elevatorsim
# @File:   buildingprofile.py
# @Time:   11/08/2021
# @Author: Gabriel O.

from dataclasses import dataclass


@dataclass
class BuildingProfile:
    teens: float
    young_adults: float
    adults: float
    older_adults: float
    elderly: float
    working_adults_ratio: float = 0.8

    def __post_init__(self):
        _sum = self.teens + self.young_adults + self.adults + self.older_adults + self.elderly
        assert (
            _sum == 1
        ), f"Bad profile: the percentages add up to {_sum * 100:.0f}%"


class StandardProfile(BuildingProfile):
    teens = 0.2
    young_adults = 0.2
    adults = 0.3
    older_adults = 0.2
    elderly = 0.1


class YoungProfile(BuildingProfile):
    teens = 0.15
    young_adults = 0.35
    adults = 0.25
    older_adults = 0.15
    elderly = 0.1


class OlderProfile(BuildingProfile):
    teens = 0.1
    young_adults = 0.1
    adults = 0.2
    older_adults = 0.25
    elderly = 0.35
