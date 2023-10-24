
#creat a class
class Panda:

#creat  4 Attributes

    def __init__(self, type:str ,weight:float , color:str , age:int ) -> None:
        self.type= type
        self.weight = weight
        self.color = color
        self.age = age

#creat 2 methods
    def Information(self):
        info = f" The {self.type} panda has a {self.weight} KG , have a {self.color} ,and {self.age} years old"
        return info


    def typePanda (self):
        type = f"the {self.type} pand have a {self.color} color"
        return type


# Create 4 instances of the class Panda
panda1 = Panda("giant", 80, "white and black " , 9)
panda2 = Panda("red ", 90, "red" , 15)
panda3 = Panda("giant", 100, " white and black " , 20)
panda4 = Panda("red ", 60 , " red" , 3)



# print 1 attribute value
print(f"the {panda3.type} pand  is {panda3.weight} kg and have a {panda3.color} color abd age {panda3.age}y years old.")



#calling 2 methods on an object
print(panda4.Information())
print(panda1.typePanda())