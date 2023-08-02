
class Trip:
    
    all = []

    def __init__(self, visitor, national_park, start_date, end_date):
        self.visitor = visitor
        self.national_park = national_park
        self.start_date = start_date
        self.end_date = end_date
        Trip.all.append(self)

    @property
    def visitor (self):
        return self._visitor
    
    @visitor.setter
    def visitor (self, visitor):
        from classes.visitor import Visitor
        if isinstance(visitor, Visitor):
            self._visitor = visitor
        else:
            raise Exception("In trip, visitor must be a visitor instance")
        
    @property
    def national_park (self):
        return self._national_park
    
    @national_park.setter
    def national_park (self, national_park):
        from classes.national_park import NationalPark
        if isinstance(national_park, NationalPark):
            self._national_park = national_park
        else:
            raise Exception("In trip, national park must be a national_park instance")

    def __repr__ (self):
        return f"Trip: {self.visitor}, {self.national_park}"
