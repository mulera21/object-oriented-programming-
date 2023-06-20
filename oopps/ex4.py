class Person(object):
    def __init__(self, name, idnumber):
        self.name = name
        self.idnumber = idnumber
    
    def display(self):
        print(self.name)
        print(self.idnumber)

    def detils(self):
        print(f"my name is {self.name}")
        print(f"idnumber is : {self.idnumber}")


man = Person("edmond", 12345)

class Employee(Person):
    def __init__(self, name, idnumber, salary, post):
        self.salary = salary
        self.post = post

        Person.__init__(self, name, idnumber)
    
    def details(self):
        print(f"my name is {self.name}")
        print(f"IdNumberr: {self.name}")
        print(f"post: {self.post}")

a = Employee("mike edwin", 54632, 20000, "intern")

a.display()
a.details()
        