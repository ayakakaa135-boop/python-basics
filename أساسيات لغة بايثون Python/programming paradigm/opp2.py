class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.__price = price
        self.quantity = quantity

    def show_info(self):
        return f"Product: {self.name}, Price: {self.__price}, Quantity: {self.quantity}"

    def set_price(self, new_price):
        self.__price = new_price
        return f"Price updated to {self.__price}"

    def get_price(self):
        return str(self.__price)+'$'

iphone_13 = Product("IPhone 13", 500, 10)

print(iphone_13.show_info())



print("Current price:", iphone_13.get_price())

iphone_13._Product__price = 0
print(iphone_13.show_info())