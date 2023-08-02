#!/usr/bin/env python3
import ipdb

from classes.national_park import NationalPark
from classes.visitor import Visitor
from classes.trip import Trip

if __name__ == '__main__':
    # print("HELLO! :) let's debug :vibing_potato:")
    john = Visitor("John")
    yoni = Visitor("Yoni")

    yosemite = NationalPark("Yosemite")
    grand_canyon = NationalPark("Grand Canyon")


    trip1 = Trip(john, yosemite, 1, 1)


    trip2 = Trip(yoni, yosemite, 1, 1)
    trip2 = Trip(yoni, yosemite, 1, 1)
    trip2 = Trip(yoni, yosemite, 1, 1)


    trip3 = Trip(yoni, grand_canyon, 1, 1)
    trip3 = Trip(yoni, grand_canyon, 1, 1)
    trip3 = Trip(yoni, grand_canyon, 1, 1)



    trip4 = Trip(yoni, yosemite, 1, 2)



    ipdb.set_trace()
