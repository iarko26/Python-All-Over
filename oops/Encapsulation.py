class car:
    def __init__(self,brand,model):
        self.__brand=brand   
        self.model=model

    
    def get_brand(self):
        return self.__brand
    


my_car=car("Audi","A4")
print(my_car.get_brand())


