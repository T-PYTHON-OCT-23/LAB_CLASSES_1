#defining a class . Always Single, we use PascalCase in naming convention
class Panda:
    def __init__(self, age:int, color:str, weight:int ,food:str):
#Attributes / Properties        
       
        self.age = age
        self.color = color
        self.weight = weight
        self.food = food
    
    def describe(self):
       describe1= f" is a {self.age}-year-old {self.color} panda weighing {self.weight} kg.{self.food} "
       return describe1
    
    def eat(self):
       food1=f"{self.color} is eating {self.food}."
       return food1
    
#creating an object of the class , new Instance of the class   
Panda1 = Panda( 20, "black and white" ,70 ,"tree leaves" )        
Panda2=  Panda( 15, "black and white" ,120 ,"plants")
Panda3=  Panda( 30, "black and white" ,70 ,"Bamboo")
Panda4=  Panda(26, "black and white" ,120 ,"sugar cane")

#accessing/reading an atttribute/property
print(Panda1.color, Panda1.age, Panda1.weight,Panda1.food)
print(Panda2.color, Panda2.age, Panda2.weight,Panda2.food)
print(Panda3.color, Panda3.age, Panda3.weight,Panda3.food)
print(Panda4.color, Panda4.age, Panda4.weight,Panda4.food)
#calling a method on an object
print(Panda1.describe())
print(Panda2.describe())
print(Panda3.eat())
print(Panda4.eat())