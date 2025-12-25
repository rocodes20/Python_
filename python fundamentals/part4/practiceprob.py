class store:
    count = 0
    def __init__(self,name,price):
        self.name = name
        self.price = price
        store.count+=1
    def get_info(self):
        print(f"{self.name} and price is ${self.price}")
    @classmethod
    def get_count(cls):
        print(cls.count)

    @staticmethod
    def discount(price,discount):
        final_price = price - (price * discount /100)
        print(final_price)
prod1 = store("pen",10)
prod2 = store("pencil",5)
store.get_count()