class Student:
    def __init__(self, name, mark):
        self.name = name
        self.__mark = mark

    def display(self):
        print("Name:", self.name)
        print("Mark:", self.mark)


s = Student("anu", 97)
s.display()

print(s.mark)  

        