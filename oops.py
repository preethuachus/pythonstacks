# class Employee:
#     id=100
#     name="aswani"
#     def display(self):
#         print(self.id,self.name)

# obj=Employee()
# b=Employee()
# obj.display()
# b.display()


# second wrk

# class Employee:
#     def __init__(self,name,id):
#         self.id=id
#         self.name=name
#     def display(self):
#         print(self.id,self.name)


# em1=Employee("aswani",11)
# em2=Employee("achu",12)
# em1.display()
# em2.display()

# thired wrk



# class Retangle:
#     def __init__(self,length,width):
#         self.length=length
#         self.width=width

#     def calculate_area(self):
#         return self.length * self.width
    

#     def display(self):
#         a=self.calculate_area()
#         print(a)

# rect=Retangle(10,5)
# rect.display()
    
#>>>>>>>>>>>>>>>>>>>>>>>>>>>  another <<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# def __str__(self):
#     area=self.calculate_area()
#     return f"Rectangle:Length={self.length},width={self.width},Area={area}"
                                                  
   
#..................... prgrams......................


# 2.Create a class SimpleInterest to calculate simple interest.
# Requirements:
# Attributes: principal, rate, time
# Method: calculate_interest() → (P × R × T) / 100
# Add str() to print all values and the interest.
        
    
# class Simpleinterest:
#     def __init__(self,principal,time,rate):
#         self.principal=principal
#         self.rate=rate
#         self.time=time

#     def calculate_interest(self):
#         e=(self.principal * self.time *self.rate)/100
#         return e
    
#     def __str__(self):
#         intert=self.calculate_interest()

#         return f"Simpleinterest:{intert} principal={self.principal},time={self.time},rate={self.rate}"
    

# a=Simpleinterest(15,20,30)
# print(a)


# 3.Temperature Converter
# Create a class Temperature to convert Celsius to Fahrenheit.
# Requirements:
# Attribute: celsius
# Method: to_fahrenheit() → (c × 9/5) + 32
# Add str() to show Celsius and Fahrenheit values.


# class Temperature :
#     def __init__(self,celsius,fahrenheit):
#         self.celsius=celsius
#         self.fahrenheit=fahrenheit

#     def calculate_temp(self):
#         a=(self.celsius* 9/5)+ 32
#         return a
    
#     def __str__(self):
#         csfa=self.calculate_temp()
#         return f"Temperature:{csfa}celsius={self.celsius},fahrenhei={self.fahrenheit}"
    
# s=Temperature(9,6)
# print(s)
        
      

# 4.Circle Area and Perimeter

# Create a Python class Circle to calculate area and perimeter of a circle.
# Requirements:
# Attribute: radius
# Methods:
# calculate_area() → π × r²
# calculate_perimeter() → 2 × π × r
# Add str() to display all results clearly.


# class circle:

#     def __init__(self,radius):
#         self.radius=radius

#     def calculate_area(self):
#         pi=3.14
#         return pi*self.radius**2
    
#     def calculate_perimeter(self):
#         pi=3.14
#         return 2*pi*self.radius
    
#     def display(self):
#         a=self.calculate_area()
#         print("area",a)
#         b=self.calculate_perimeter()
#         print("perimeter",b)

# s=circle(5)
# s.display()


# 6.Car Mileage Calculator
# Create a class Car to calculate mileage.
# Requirements:
# Attributes:
# car_name
# distance_travelled (in km)
# fuel_used (in liters)
# Method:
# calculate_mileage() → distance / fuel
# Add str() to display mileage clearly.


# class car :
#     def __init__(self,carname,distance,fuel):
#         self.carname=carname
#         self.distance=distance
#         self.fuel=fuel

#     def calculate_milage(self):
#         return self.distance / self.fuel
    
#     def display(self):
#         print("carname:",self.carname)
#         print("distance",self.distance)
#         print("fuel",self.fuel)
#         print("milage",self.calculate_milage)


# s=car("swift",300,15)
# s.display()


# 5.Bank Account System

# Create a class BankAccount to simulate deposit and withdrawal operations.
# Requirements:
# Attributes: account_holder, balance
# Methods:
# deposit(amount)
# withdraw(amount) → check for sufficient balance
# display_balance()
# Add str() to show account details.

# class bankaccount:
#     def __init__(self,account_holder , balance=0):
#         self.account_holder =account_holder
#         self.balance =balance

#     def dsposite(self,amount):
#         self.balance+=amount
#         print("deposited")

#     def widraw(self,amount):
#         if amount > self.balance:
#             print("insufficient balance")
#         else:
#             self.balance-=amount
#             print("succesfully")

# b=bankaccount("preethu")
# b.dsposite(1000)
# b.widraw(1500)
           

        
       

        
        
    
        

    

        
        
