class car:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
    def fullname(self):
        return f"{self.brand} {self.model}"

        
class electric_car(car):
    def __init__(self,brand,model,battery_size):
        super().__init__(brand,model)
        self.battery_size=battery_size

my_car=car("Audi","A4")
print(my_car.brand)
print(my_car.fullname())
mytesla=electric_car("Tesla","Model S",75)
print(mytesla.battery_size)
