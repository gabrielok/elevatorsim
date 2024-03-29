# elevatorsim
# @File:   buildingprofile.py
# @Time:   11/08/2021
# @Author: Gabriel O.

from dataclasses import dataclass, field

from .exceptions import BadProfileException


@dataclass
class BuildingProfile:
    """
    Abstract class for defining profiles of the residents of a building. A profile must
    define which fraction of the residents belongs to each age group:
        + Teens: up to 17 years old
        + Young adults: 17-25 years old
        + Adults: 25-45 years old
        + Older adults: 45-65 years old
        + Retired: older than 65
    A profile may define:
        + which fraction of the working age groups works out of home
    """

    teens: float = field(init=False)
    young_adults: float = field(init=False)
    adults: float = field(init=False)
    older_adults: float = field(init=False)
    retired: float = field(init=False)
    employment_ratio_young_adults: float = 0.80
    employment_ratio_adults: float = 0.75
    employment_ratio_older_adults: float = 0.70
    employment_ratio_retired: float = 0.55

    def __post_init__(self):
        _sum = (
            self.teens
            + self.young_adults
            + self.adults
            + self.older_adults
            + self.retired
        )
        if abs(_sum - 1) > 1e-3:
            raise BadProfileException(_sum)


class StandardProfile(BuildingProfile):
    teens = 0.15
    young_adults = 0.2
    adults = 0.3
    older_adults = 0.2
    retired = 0.15


class YoungProfile(BuildingProfile):
    teens = 0.15
    young_adults = 0.35
    adults = 0.25
    older_adults = 0.15
    retired = 0.1


class OlderProfile(BuildingProfile):
    teens = 0.1
    young_adults = 0.1
    adults = 0.2
    older_adults = 0.25
    retired = 0.35
