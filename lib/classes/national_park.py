from classes.trip import Trip


class NationalPark:
    def __init__(self, name):
        self.name = name

    def total_visits(self):
        return len(self.trips())
    
    def best_visitor(self):
        return max(set([trips.visitor for trips in self.trips()]), key=[trips.visitor for trips in self.trips()].count)

    @classmethod
    def most_visited(cls):
        return max(set([trips.national_park for trips in Trip.all]), key=[trips.national_park for trips in Trip.all].count)

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if hasattr(self, "name"):
            raise Exception ("Can't rename national park")
        else:
            self._name = name
    
    def trips(self):
        return [trips for trips in Trip.all if trips.national_park == self]
    
    def visitors(self):
        return list(set([trips.visitor for trips in self.trips()]))

    def __repr__ (self):
        return f"National Park: {self.name}"