class car:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
    def fullname(self):
        return f"{self.brand} {self.model}"

        
    

my_car=car("Audi","A4")
print(my_car.brand)
print(my_car.fullname())


