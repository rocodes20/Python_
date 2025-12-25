class Laptop:
    storage = "ssd"
    @classmethod
    def get_storage(cls):
        print(f"{cls.storage}")
    def __init__(self,ram,gen):
        self.ram = ram
        self.gen = gen
    
    def get_info(self): #instance method
        print(f"laptop has {self.ram} RAM , {self.storage} and is {self.gen}")

    @staticmethod
    def discount(price,discount):
        final_price = price - (price * discount / 100)
        print(final_price)


   

lap1 = Laptop("8gb","i7")
lap1.get_info()
lap1.get_storage()
lap1.discount(40000,10)
