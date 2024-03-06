class Univercity:
    def __init__(self, univercity) -> None:
        self.univercity = univercity
        
    def __str__(self) -> str:
        return f"""
        Univercity: {self.univercity}"""
    
class Staff(Univercity):
    def __init__(self, univercity, first_name, last_name, age) -> None:
        super().__init__(univercity)
        self.fname = first_name
        self.lname = last_name
        self.age = age

    def __str__(self) -> str:
        return f"""        {super().__str__()}
        First name: {self.fname}
        Last name: {self.lname}
        Age: {self.age}"""
    
class Student(Staff):
    def __init__(self, univercity, first_name, last_name, age,group) -> None:
        super().__init__(univercity, first_name, last_name, age)
        self.group = group

    def __str__(self) -> str:
        return f"""{super().__str__()}
        Group: {self.group}
        """
    
class Teacher(Staff):
    def __init__(self, univercity, first_name, last_name, age, position,subject) -> None:
        super().__init__(univercity, first_name, last_name, age)
        self.position = position
        self.subject = subject

    def __str__(self) -> str:
        return f"""{super().__str__()}
        Position: {self.position}
        Subject: {self.subject}
        """
class OtherStaff(Staff):
    def __init__(self, univercity, first_name, last_name, age, position) -> None:
        super().__init__(univercity, first_name, last_name, age)
        self.position = position

    def __str__(self) -> str:
        return f"""        {super().__str__()}
        Position: {self.position}"""
    
univer = Student("Najot ta`lim", "Farrux", "Umarov", 31, "N66")

univer1 = Teacher("Najot ta`lim", "Aziz", "Shakirov", 35, "Senior", "programmer")

univer2 = OtherStaff("Najot ta`lim", "Akmal", "Qurbonov", 27, "N48")

print("         <<< Student >>>")
print(univer)

print("         <<< Teacher >>>")
print(univer1)

print("         <<< another class student >>>")
print(univer2)