class Employe:
    def __init__(self, Surname, Position, Salary) -> None:
        self.name = Surname
        self.position = Position
        self.salary = Salary

class Enterprise_employee(Employe):
    def __init__(self, Surname, Position, Salary, Rating) -> None:
        super().__init__(Surname, Position, Salary)
        self.rating = Rating
        

    def info(self):
        return f"""
        Surname {self.name}
        Position {self.position}
        Salary {self.salary}
        Rating {self.rating}
"""
    def salar(self):

        if self.rating < 100:
            
            if self.rating > 60 and self.rating < 75:
                self.salary *= 1.2
            elif self.rating >= 75 and self.rating < 90:
                self.salary *= 1.4
            elif self.rating >= 90 and self.rating <= 100:
                self.salary*=1.6
                
            return self.info()
        else: return """
                Kiritilgan bonus 100dan baland !!! 
            Iltimos 100dan kichik bonus kiriting!!!
            """
        


lst = list()    

for emplo in range(2) :      
    name = input("Enter Surname: ")
    position = input("Enter Position: ")
    salary = int(input("Enter Salary: "))
    rating = int(input("Enter Rating: "))

    employe = Enterprise_employee(name, position, salary, rating)
    lst.append(employe.salar())



for emplo in lst:
    print(emplo)