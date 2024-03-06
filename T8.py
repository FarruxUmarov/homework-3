class Transport:
    def __init__(self, brand, model, type) -> None:
        self.brand = brand
        self.model = model
        self.type = type

    def __str__(self):
        return f"""
        Brand: {self.brand}
        Model: {self.model}
        Type: {self.type}"""
    
class ElectroCars(Transport):
    def __init__(self, brand, model, type, battery_life, chargin_time) -> None:
        super().__init__(brand, model, type)
        self.battery = battery_life
        self.chargin = chargin_time

    def __str__(self) -> str:
        return f"""
        {super().__str__()}
        battery life: {self.battery}
        chargin time: {self.chargin}
        """
    
class SportCars(Transport):
    def __init__(self, brand, model, type, motor, color) -> None:
        super().__init__(brand, model, type)
        self.motor = motor
        self.color = color

    def __str__ (self) -> str:
        return f"""
        {super().__str__()}
        Motor: {self.motor}
        Color: {self.color}
        """
    
class Truck(Transport):
    def __init__(self, brand, model, type, motor,height, long,wieght) -> None:
        super().__init__(brand, model, type)
        self.moto = motor
        self.height = height
        self.long  = long
        self.wieght = wieght

    def __str__ (self) -> str:
        return f"""
        {super().__str__()}
        Motor: {self.moto}
        Height: {self.height}
        Long: {self.long}
        wieght: {self.wieght}
        """

print("         <<< Electro car >>>")
elekrto = ElectroCars("Lion", "A33", "Electro_mobile", 180000, 15)
print(elekrto)

print("         <<< Sport car >>>")
elekrto1 = SportCars("Mustang", "G200", "Sport car", 4.8, "Black")
print(elekrto1)

print("         <<< Truck >>>")
elekrto2 = Truck("Merc", "AAAC", "Truck", 15.3, 3, 17, 8)
print(elekrto2)


    




# transport = Transport("samsung", "s20", "asdas")

# print(transport.info())
    
















#     def __str__(self)-> str:
#         return f"""
# Brand: {self.brand}
# Model: {self.model}
# Type: {self.type}
# """"