class Product:
    def __init__(self, price):
        self.price = price
        
    @property
    def price(self):
        return self.__price
    
    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Price Cannot be Negative")
        if value == 0:
            raise ValueError("Price cannot be zero")
        self.__price = value
    def __str__(self):
        return f"Product Price: {self.price}"

price = float(input("Enter Price: "))
product = Product(price)  