


class Auto():
    def __init__(self, make, model, year, color, num_wheels):
        self.make = make
        self.model = model
        self.year = year
        self.color = color
        self.num_wheels = num_wheels
        
    def drive(self):
        print("WE ARE DRIVING", self.model)

    def advertise(self):
        print("BUY OUR", self.model)
    
class Truck(Auto):
    def __init__(self, make, model, year, color, num_wheels, bed_size):
        super().__init__(make, model, year, color, num_wheels)
        self.bed_size = bed_size

    def advertise(self):
        print("VROOOOM", self.model)


if __name__ == "__main__":


    car = Auto("Toyota", "Prius", 2020, "Blue", 4)
    car.drive()
    car.advertise()
    car2 = Auto("Tesla", "Model S", 2020, "Blue", 4)
    car2.drive()
    car2.advertise()
    truck = Truck("Ford", "F150", 2020, "Blue", 4, bed_size="5x5")
    truck.drive()
    truck.advertise()
    print(truck.bed_size)
    truck2 = Truck("Tesla", "Cybertuck", 2020, "Blue", 4, bed_size="10x10")
    truck2.drive()
    truck2.advertise()
    print(truck2.bed_size)