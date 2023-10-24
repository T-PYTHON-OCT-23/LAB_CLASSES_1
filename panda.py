#creat class

class Panda:

    def __init__(self, type:str, age:int, weight:int, color:str):
        self.type = type
        self.age = age 
        self.weight = weight
        self.color = color

    def str_information(self):
        str_information = f"This type of panda is{self.type}, there color is {self.color}"
        return str_information
    
    def num_information(self):
        num_information = f"theire ages range from {self.age} years, there weight are between {self.weight} Kg"
        return num_information
    
panda1 = Panda("melanoleuca", 20, 150, "black and white")
panda2 = Panda("Ailurus fulgens", 23, 6,"brown and red")
panda3 = Panda("Ailuropoda baconi", 20, 120, "black and white")
panda4 = Panda("wulingshanensis", 22, 95, "White")

print(panda1.type, panda1.age, panda1.weight, panda1.color)
print(panda2.type, panda2.age, panda2.weight, panda2.color)
print(panda3.type, panda3.age, panda3.weight, panda3.color)
print(panda4.type, panda4.age, panda4.weight, panda4.color)

print(panda1.str_information())
print(panda1.num_information())

print(panda2.str_information())
print(panda2.num_information())

print(panda3.str_information())
print(panda3.num_information())

print(panda4.str_information())
print(panda4.num_information())