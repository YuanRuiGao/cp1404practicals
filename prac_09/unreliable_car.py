from prac_09.car import Car
import random


class UnreliableCar(Car):
    def __init__(self, name, fuel, reliability):
        """The subclass inherits the initial value from the parent class and a new value"""
        super().__init__(name, fuel)
        self.reliability = float(reliability)

    def drive(self, distance):
        """drive the car with a given distance"""
        number = random.randint(0, 100)
        if number < self.reliability:
            distance = distance
        else:
            distance = 0
        return distance
