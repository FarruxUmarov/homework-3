class Book:
    def __init__(self, name, page_count, price) -> None:
        self.name = name
        self.page = page_count
        self.price = price

    def __str__(self) -> str:
        return f"""
            <<< Book >>> 
               
        Name book: {self.name}
        Page count: {self.page}
        Price: {self.price}"""

    def Kitob():
        kitoblar = list()
        kitob = int(input("Kitob sonini kiriting: "))

        for _ in range(kitob):
            name = input("Kitob nomini kiriting: ")
            page = int(input("kitob betlar sonini kiriting: "))
            price = int(input("Kitob narxini kiriting: "))

            kitoblar.append(Book(name,page,price))
        return kitoblar
    
    def ten(self):
        self.page += 10
        return self.page
    
    def update(self):
        if self.page > 100:
            self.price //= 2

book = Book.Kitob()

for k in book:
    k.ten()
    k.update()
    print(k)

        
    