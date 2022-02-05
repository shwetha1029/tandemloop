print("A basic calculator, \nYour options are:")
class Cals():
    def __init__(self,a,b):
        self.a = a
        self.b = b
    def add(self):
        return self.a + self.b
    def sub(self):
        return self.a - self.b
    def multiply(self):
        return self.a * self.b
    def divide(self):
        return self.a / self.b


while True:
    def menu():
        x = ('1. Add \n2. Sub \n3. Multiply \n4. Divide.\n0. Exit') 
        print(x)
    menu()
    choice = int(input('Please select one of the above option: '))
    if choice == 1:
        a = float(input('Enter First number value: '))
        b = float(input('Enter Second number value: '))
        obj=Cals(a,b)
        print("Result: ",obj.add())
    elif choice == 2:
        a = float(input('Enter First number value: '))
        b = float(input('Enter Second number value: '))
        obj=Cals(a,b)
        print("Result: ",obj.sub())
    elif choice == 3:
        a = float(input('Enter First number value: '))
        b = float(input('Enter Second number value: '))
        obj=Cals(a,b)
        print("Result: ",obj.multiply())    
    elif choice == 4:
        a = float(input('Enter First number value: '))
        b = float(input('Enter Second number value: '))
        obj=Cals(a,b)
        print("Result: ",obj.divide())
    elif choice == 0:
        print('Thank you, Goodbye')
        break
    else:
        print('Invalid option') 
        break 
