from classes.trip import Trip


class Visitor:
    def __init__(self, name):
        self.name = name

    def trips(self):
        pass

    def national_parks(self):
        pass

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name (self, name):
        if type(name) == str and 1 <= len(name) <= 15:
            self._name = name
        else:
            raise Exception("Name must be a string between 1-15 characters")
    
    def trips(self):
        return [trip for trip in Trip.all if trip.visitor == self]
    
    def national_parks(self):
        return list(set([trip.national_park for trip in self.trips()]))
        
    def __repr__ (self):
        return f"Visitor: {self.name}"