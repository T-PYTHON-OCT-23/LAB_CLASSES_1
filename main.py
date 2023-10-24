# LAB_CLASSES_1


class Panda:

    def __init__(self, type:str , age:int ,gender:str ,live:str):

        self.type=type
        self.age=age
        self.gender=gender
        self.live=live

    #create two methods 

    def eat(self ,food):
        print(f"Panda is eating {food}")

    def typeOfpanda(self):
        typePan=f"{self.type}"
        return typePan
    
# 4 instances 
panda1=Panda('Giant panda',6 , 'male','china')
panda2=Panda('Red panda',10 , 'female','india')
panda3=Panda('Qinling panda',15 , 'female','china')
panda4=Panda('Giant panda',3 , 'male','india')

print( "panda 1 live in : ",panda1.live)
print("panda 2 age is : ",panda2.age)
print("panda 3 gender is  : ",panda3.gender )



panda1.eat("apples")
print(f"Fourth Panda is : {panda4.typeOfpanda()}")

#panda2.typeOfpanda()

#print(f"First Panda is : {panda1.typeOfpanda()} he is  {panda1.age} years old ")
#print(f"Second Panda is : {panda2.typeOfpanda()} she is {panda2.gender}")
#print(f"Third Panda is : {panda3.typeOfpanda()} and she lives in {panda3.live}")
#print(f"Fourth Panda is : {panda4.typeOfpanda()}, {panda4.info()}, {panda4.age}")














    


