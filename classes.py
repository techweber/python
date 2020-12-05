class Person:
    def __init__(self,fname,lname):
        self.fname = fname
        self.lname = lname

    def printname(self):
        print(self.fname, self.lname)

class Student(Person):
    def __init__(self, fname, lname, year):
        self.fname = fname
        self.lname = lname
        self.year = year

    def hello(self):
        print('hello', self.fname, self.lname, 'to the year of ', self.year)

x = Student("Mike", "Gates", 2015)

x.hello()


