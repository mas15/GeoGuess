import itertools

class Puzzle():
    def __init__(self, location_to_guess, start_location):
        self.location_to_guess = location_to_guess
        self.start_location = start_location


class Location():
    next_id = itertools.count().next

    def __init__(self, name, latitude, longitude):
        self.id = Location.next_id()
        self.name = name
        self.latitude = latitude
        self.longitude = longitude