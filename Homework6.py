#1. Write a python class to find max, min num and sum in your list: don’t use max sum and min function
class Operacions:
    def __init__(self, num_list):
        self.num_list = num_list
        
    def max_num(self):
        self.num_list.sort()
        return self.num_list[-1]
    
    def min_num(self):
        self.num_list.sort()
        return self.num_list[0]
    def sum_of_num(self):
        summa = 0
        for i in self.num_list:
            summa += i
        return summa
a = Operacions([-5, 3, 11, 96, -23, 1, 6, 9])
print(a.max_num())
print(a.min_num())
print(a.sum_of_num())

#2. Write a python class to find two highest values in your dict:
class HighestValue:
    def __init__(self, dictionary):
        self.dictionary = dictionary
    
    def find_values(self):
        values = list(self.dictionary.values())
        values.sort()
        return values[-1], values[-2]

b = HighestValue({'f': 45, 'w': 196, 'b': -32, 'c': 0, 'r': 79, 'k': 781})
print(b.find_values())

#3. Write a python class where your child class takes all methods in parent class and print them.
class Parent:
    def __init__(self, num_list):
        self.num_list = num_list
        
    def max_num(self):
        self.num_list.sort()
        return self.num_list[-1]
    
    def min_num(self):
        self.num_list.sort()
        return self.num_list[0]
    def sum_of_num(self):
        summa = 0
        for i in self.num_list:
            summa += i
        return summa
        
class Child(Parent):
    def __init__(self, num_list):
        super().__init__(num_list)        

#4.  Write a Python class named Rectangle constructed by a length and width and a method which will compute the area of a rectangle.
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

r = Rectangle(5, 4)
print(r.area())


#5. Write a python class where we use polymorphism:
#Example:
#a.country() - Erevan
#b.country() - Paris
class Armenia:
    def capital(self):
        print('Yerevan')

class Russia:

    def capital(self):
        print('Moscow')


a = Armenia()
b = Russia()
a.capital()
b.capital()

#6.  Create a class Change:You have 3 methods in your class:
#Usd --- Eur
#Usd --- Amd
#Usd --- R
class Change:
    def __init__(self, usd):
        self.usd = usd

    def usd_to_eur(self):
        exchange = 0.85
        return self.usd * exchange

    def usd_to_amd(self):
        exchange = 485.0
        return self.usd * exchange

    def usd_to_r(self):
        exchange = 0.74
        return self.usd * exchange
c = Change(100)
print(c.usd_to_eur())
print(c.usd_to_amd())
print( c.usd_to_r())