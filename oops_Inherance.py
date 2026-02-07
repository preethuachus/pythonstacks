# SINGLE

# class Animal:
#     def speak(self):
#         print("animal speaking")

# class Dog (Animal):
#     def bark(self):
#         print("dog barking")

# d=Dog()
# d.speak()
# d.bark()


# MUTIPLE

# class animal:
#     def speak(self):
#         print("animal speaking")

# class dog(animal):
#     def bark(self):
#         print("dog barking")

# class dogchild(dog):
#     def eat(slef):
#         print("dog eats")
# d=dogchild()
# d.bark()
# d.speak()
# d.eat()

# MULTILEVEL

# class calculation1:
#     def add(self,a,b):
#         return a+b
    
# class calculation2:
#     def mul(self,a,b):
#         return a*b
    
# class Divided (calculation1,calculation2):
#     def divide(self,a,b):
#         return a/b
    
# a=Divided()
# print(a.add(10,20))
# print(a.mul(2,3))
# print(a.divide(10,3))


# HIERARCHY

# class parent:
#     def fun1(self):
#         print("this is parent class")


# class child1(parent):
#     def ch1(self):
#         print("this is child1")

# class child2(parent):
#     def ch2(self):
#         print("this is child2")


# ob1=child1()
# ob2=child2()
# ob1.ch1()
# ob1.fun1()
# ob2.ch2()
# ob2.fun1()


# HYBRIDE

# class Animal:
#     def speak(self):
#         print("Animal speaking")

# class Cat(Animal):
#     def birth(self):
#         print("Cat gives birth")

# class Bird(Animal):
#     def egg(self):
#         print("Bird lays eggs")


# class PlayHome(Cat, Bird):
#     def eat(self):
#         print("Play and eat")


# p = PlayHome()

# p.speak()   
# p.birth()   
# p.egg()     
# p.eat()    
# 
# 
# 
# Q1. Create a Base class Animal with a method sound(). Create a Derived class Dog that prints “Bark” using inheritance. 


# class animal:
#     def sound(self):
#         print("animal sound")

# class Dog(animal):
#     def bark(self):
#         print("Dog barking")


# d=Dog()
# d.sound()
# d.bark()

# Q2. Create a class Vehicle with attributes brand and model. Create another class Car that inherits and displays the full car details.

# class Vehicle:
#     def __init__(self, brand, model):
#         self.brand = brand
#         self.model = model


# class Car(Vehicle):
#     def display(self):
#         print("Car Brand:", self.brand)
#         print("Car Model:", self.model)


# c = Car("Toyota", "Innova")
# c.display()


# Q3. Create classes: LivingThing → Animal → Dog. Each class should have one method. Call all methods using a Dog object.


# class LivingThing:
#     def add(self,a,b):
#         print(a+b)
    

# class animal(LivingThing):
#     def mul(self,a,b):
#         print(a*b)
    
# class dog(animal):
#     def divided(self,a,b):
#         print(a/b)


# d=dog()
# d.add(2,3)
# d.mul(5,4)
# d.divided(3,9)


# Q4. Create classes: College → Department → Student. Print college name, department name, and student name.
    

# class Collage:
#     def collage_name(self):
#         print("College Name: ABC College")


# class Department(Collage):
#     def department_name(self):
#         print("Department Name: Computer Science")


# class Student(Department):
#     def student_name(self):
#         print("Student Name: preethu")

# S=Student()
# S.department_name()
# S.collage_name()
# S.student_name()


# Q5. Create class Animal with method eat(). Inherit into Dog and Cat classes, and each prints its own sound. 
# class Animal:
#     def eat(self):
#         print("Animal is eating")


# class Dog(Animal):
#     def sound(self):
#         print("Dog says: Bark")


# class Cat(Animal):
#     def sound(self):
#         print("Cat says: Meow")

# d = Dog()
# d.eat()
# d.sound()

# c = Cat()
# c.eat()
# c.sound()

# Q6. Create class Shape inherited by Circle, Rectangle, and Triangle and each calculates area separately.


# class Shape:
#     pass

# class Circle(Shape):
#     def area(self, r):
#         print("Circle Area:", 3.14 * r * r)

# class Rectangle(Shape):
#     def area(self, l, w):
#         print("Rectangle Area:", l * w)

# class Triangle(Shape):
#     def area(self, b, h):
#         print("Triangle Area:", 0.5 * b * h)


# c = Circle()
# r = Rectangle()
# t = Triangle()

# c.area(5)
# r.area(4, 6)
# t.area(3, 8)














# Q7. Create class Father and class Mother. Create class Child that inherits both and prints traits from each parent.

# class Father:
#     def trait_father(self):
#         print("Father's trait: Strong")

# class Mother:
#     def trait_mother(self):
#         print("Mother's trait: Caring")

# class Child(Father, Mother):
#     def trait_child(self):
#         print("Child inherits traits from both")

# c = Child()
# c.trait_father()
# c.trait_mother()
# c.trait_child()

# Q8. Create class A with a method displayA() and class B with displayB(). Class C should inherit both and call both methods.

# class A:
#     def displayA(self):
#         print("This is Class A")

# class B:
#     def displayB(self):
#         print("This is Class B")

# class C(A, B):
#     def displayC(self):
#         print("This is Class C")

# obj = C()
# obj.displayA()
# obj.displayB()
# obj.displayC()


# Q9. Create a base class Person, derive Student and Employee. Then from Student, derive Intern. Print details from all levels.

# class Person:
#     def __init__(self, name):
#         self.name = name

#     def show_person(self):
#         print("Name:", self.name)

# class Student(Person):
#     def __init__(self, name, roll):
#         super().__init__(name)
#         self.roll = roll

#     def show_student(self):
#         print("Roll No:", self.roll)

# class Employee(Person):
#     def __init__(self, name, emp_id):
#         super().__init__(name)
#         self.emp_id = emp_id

#     def show_employee(self):
#         print("Employee ID:", self.emp_id)

# class Intern(Student):
#     def __init__(self, name, roll, duration):
#         super().__init__(name, roll)
#         self.duration = duration

#     def show_intern(self):
#         print("Internship Duration:", self.duration)

# i = Intern("Preethu", 101, "6 Months")
# i.show_person()
# i.show_student()
# i.show_intern()


# Q10. Create classes: A as base → B and C inherit from A → D inherits from both B and C. Call methods from all.

# class A:
#     def showA(self):
#         print("Class A")

# class B(A):
#     def showB(self):
#         print("Class B")

# class C(A):
#     def showC(self):
#         print("Class C")

# class D(B, C):
#     def showD(self):
#         print("Class D")

# obj = D()
# obj.showA()
# obj.showB()
# obj.showC()
# obj.showD()



