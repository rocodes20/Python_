#wrapping up data and functions in single unit
class BankAccount:
    def __init__(self,name,balance):
        self.name = name
       # self._balance = balance #protected
        self.__balance = balance # private

    def get_balance(self): #getter
        return self.__balance
    
acc1 = BankAccount("Rohit",100_000)
print(acc1.name,acc1.get_balance())



#public by default every attribute is public
#private done with __ giving access only to its class
#protected is private but access is give to its class and the child class
