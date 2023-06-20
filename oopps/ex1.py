class Dog:
    
    attr1 = "mammal"

    def __init__(self, name):

        self.name = name


Rodger = Dog("kenny")
Tommy = Dog("mike")

print("Rodger is a {}".format(Rodger.__class__.attr1))

print("Rodger is a {}".format(Tommy.__class__.attr1))

print(f"my name is {Rodger.name}")
print(f"my name is {Tommy.name}")