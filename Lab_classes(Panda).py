#LAB-CLASSES-(PANDA)
class Panda:

    def __init__(self, name:str, length:str, size:str, country:str ):
        #Attributes
        self.name = name
        self.length = length
        self.size = size
        self.country = country

    #Creating meathods 
    def first_behavior(self):
        condition = f"The {self.name} are not active and spend most of their time eating and sleeping."
        return condition
    def second_behavior(self):
        eat = f"The {self.name} eats Bambo."
        return eat

Panda1 = Panda("Ailuropoda melanoleuca"," 6 feet long","Big","Southwest China")
Panda2 = Panda("Ailurus fulgens", " 22 to 24.6 inch "," Small","Eastern Himalayas")

#Reading Attributes
print(Panda1.name, Panda1.length, Panda1.size , Panda1.country)
print(Panda2.name, Panda2.length, Panda2.size , Panda2.country)

#Calling methods
print(Panda1.first_behavior())
print(Panda2.second_behavior())
