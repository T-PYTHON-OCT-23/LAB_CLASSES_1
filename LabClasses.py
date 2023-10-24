class Panda:

    def __init__(self, name:str, color:str ,age:int,length:float):
        self.name=name
        self.color=color
        self.age=age
        self.length=length
    
    def speed(self):
        speed_panda= f"This Panda {self.name} and age is {self.age} , {self.length} m reach a speed of 32 Km/hour"
        return speed_panda
    
    def mPanda(self):
        pandaFeet= f"This Panda {self.name} and age is  {self.age} , {self.color} ,{self.length} m has 6 toes on its front feet"
        return pandaFeet
    
Panda1=Panda("Giant panda","black",10,1.5)
Panda2=Panda("mala panda","black",5,1.8)
Panda3=Panda("Female panda","black & white",10 , 2)
Panda4=Panda("Male panda","black & white",3 , 2.5)

print(f"Hi you have info about this panda {Panda1.name} : {Panda1.speed()}")
print(f"Hi you have info about this panda {Panda2.name} : {Panda2.speed()}")
print(f"Hi you have info about this panda {Panda3.name} : {Panda3.speed()}")
print(f"Hi you have info about this panda {Panda4.name} : {Panda4.speed()}")