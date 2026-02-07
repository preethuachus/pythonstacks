class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model
        self.__speed = 0   # Encapsulated (private) variable

    # Abstracted method - user doesn't see internal logic
    def accelerate(self, increase):
        self.__speed += increase
        print(f"Accelerated by {increase} km/h. Current speed: {self.__speed} km/h")

    # Abstracted method - hiding how speed can't go negative
    def brake(self, decrease):
        self.__speed -= decrease
        if self.__speed > 0:
            print(f"Braked by {decrease} km/h. Current speed: {self.__speed} km/h")
        else:
            self.__speed = 0
            print(f"Speed: {self.__speed} km/h (Car stopped)")

    def display_speed(self):
        print(f"{self.make} {self.model} is moving at {self.__speed} km/h")



car1 = Car("Toyota", "Camry")

car1.display_speed()
car1.accelerate(30)
car1.brake(10)
car1.display_speed()
