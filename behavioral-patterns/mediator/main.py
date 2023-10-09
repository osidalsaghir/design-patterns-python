class AirTrafficControl:
    def __init__(self):
        self.runway = None
        self.taxiway = None
        self.airplanes = []

    def assign_runway(self, airplane):
        self.runway = airplane
        self.runway.land()

    def assign_taxiway(self, airplane):
        self.taxiway = airplane
        self.taxiway.taxi()

    def register_airplane(self, airplane):
        self.airplanes.append(airplane)

class Airplane:
    def __init__(self, name):
        self.name = name

    def land(self):
        print(f"{self.name} is landing on the runway.")

    def taxi(self):
        print(f"{self.name} is taxiing on the taxiway.")

if __name__ == "__main__":
    atc = AirTrafficControl()

    plane1 = Airplane("Flight 123")
    plane2 = Airplane("Flight 456")

    atc.register_airplane(plane1)
    atc.register_airplane(plane2)

    atc.assign_runway(plane1)
    atc.assign_taxiway(plane2)
