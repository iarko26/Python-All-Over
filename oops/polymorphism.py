class car:
    def __init__(self,brand,model):
        self.__brand=brand   
        self.model=model

    
    def get_brand(self):
        return self.__brand
    
    def fuel_type(self):
        return "Petrol"

class electric_car(car):
    def __init__(self,brand,model,battery_size):
        super().__init__(brand,model)
        self.battery_size=battery_size
    def fuel_type(self):
        return "Electric"
    

    


my_car=car("Audi","A4")
print(my_car.fuel_type())
mytesla=electric_car("Tesla","Model S",75)
print(mytesla.fuel_type())