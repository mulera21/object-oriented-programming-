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

man.display()
man.detils()
    

        