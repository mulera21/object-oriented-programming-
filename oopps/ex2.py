class Dog:
    attr1 = "mammal"

    def __init__(self, name):
        self.name = name
    def speak(self):
        print("my name is {}".format(self.name))

tin = Dog('PETER')
vin = Dog("MIKE")

tin.speak()
vin.speak()