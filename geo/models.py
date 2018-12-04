import itertools


class Puzzle:
    def __init__(self, location_to_guess, start_location):
        self.location_to_guess = location_to_guess
        self.start_location = start_location


class Location:
    last_id = itertools.count()

    def __init__(self, name, latitude, longitude):
        self.id = next(Location.last_id)
        self.name = name
        self.latitude = latitude
        self.longitude = longitude
