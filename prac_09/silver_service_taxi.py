from prac_09.taxi import Taxi


class SilverServiceTaxi(Taxi):
    flagfall = 4.50

    def __init__(self, name, fuel, fanciness):
        """Inheriting data from a parent class"""
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.price_per_km = Taxi.price_per_km * fanciness

    def __str__(self):
        """Returns a string"""
        return (f"{self.name}, fuel={self.fuel}, odometer={self.current_fare_distance}, {self.get_fare()}"
                f"km on current fare, ${self.price_per_km}/km plus flagfall of ${self.flagfall}")

    def get_fare(self):
        """Return the added flagfall"""
        return super().get_fare() + self.flagfall


