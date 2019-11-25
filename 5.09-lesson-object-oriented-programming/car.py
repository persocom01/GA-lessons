class AdvancedCar:
    """
    A more advanced Car class that features gasoline tracking.
    """

    def __init__(self, make, model, mpg, tank_size):
        self.make = make
        self.model = model
        self.mpg = mpg
        self.gas = self.tank_size = tank_size
        self.miles = 0
        self.on = False

    def honk(self):
        print("Beep beep!")

    def turn_on(self):
        self.on = True

    def turn_off(self):
        self.on = False

    def drive(self, distance):
        """
        Advance the car `distance` miles. If the car is off, or if there is
        insufficient gas remaining, an error is thrown.
        """
        if self.on:
            gas_used = distance / self.mpg
            if gas_used <= self.gas:
                self.gas -= gas_used
                self.miles += distance
            else:
                raise InsufficientGasError("You don't have enough gas!")
        else:
            raise CarOffError("The car is off!")

    def fill_tank(self, gallons):
        """
        Adds `gallons` gallons to the tank. If this would exceed the maximum
        tank size, the tank is simply filled.
        """
        self.gas = min(self.gas + gallons, self.tank_size)

class CarOffError(Exception):
    pass

class InsufficientGasError(Exception):
    pass

