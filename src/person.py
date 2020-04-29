class Person:

    def __init__(self,name,height):
        self.name = name
        self.height = height

    def get_height(self):
        return self.height

    def __str__(self):
        return self.name + " is " + str(self.height) + "cm tall"
