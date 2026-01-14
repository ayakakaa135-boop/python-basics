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



class Mobile(Product):
    def __init__(self, name, __price, quantity, camera, battery):
        super().__init__(name, __price, quantity)
        self.camera = camera
        self.battery = battery

    def show_info(self):
        base = super().show_info()
        return f"{base}, Camera: {self.camera}, Battery: {self.battery}"

    def specs(self):
        return (
            f"📱 {self.name} Specifications:\n"
            f"💰 Price: {self.__price} USD\n"
            f"📦 Quantity: {self.quantity}\n"
            f"📸 Camera: {self.camera}\n"
            f"🔋 Battery: {self.battery}\n"

        )
class Laptop(Product):
    def __init__(self, name, __price, quantity, ram, storage):
        super().__init__(name, __price, quantity)
        self.ram = ram
        self.storage = storage

    def show_info(self):
        base = super().show_info()
        return f"{base}, RAM: {self.ram}, Storage: {self.storage}"


class Monitor(Product):
    def __init__(self, name, __price, quantity, size, refresh_rate):
        super().__init__(name, __price, quantity)
        self.size = size
        self.refresh_rate = refresh_rate

    def show_info(self):
        base = super().show_info()
        return f"{base}, Size: {self.size}, Refresh Rate: {self.refresh_rate}Hz"
laptop = Laptop("Dell XPS", 1500, 3, "16GB", "512GB SSD")
mobile = Mobile("iPhone 15", 1200, 5, "48MP", "4000mAh")
monitor = Monitor("Samsung 4K", 700, 2, "27 inch", 144)

print(laptop.show_info())
print(mobile.show_info())
print(monitor.show_info())
l1= Laptop("Dell XPS", 1500, 3, "16GB", "512GB SSD")
m1 = Mobile("iPhone 15", 1200, 5, "48MP", "4000mAh")
print(m1.specs())


