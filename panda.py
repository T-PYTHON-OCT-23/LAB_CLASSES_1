class Panda:
    def __init__(self,type:str,age:int,gender,extinct_or_alive:str):
        self.type= type
        self.age= age
        self.gender=gender
        self.extinct_or_alive=extinct_or_alive

Panda1 =Panda("Ailuropoda melanoleuca",19,"male","existent")
Panda2=Panda("Red panda",5,"male","Threatened with extinction")
Panda3=Panda("Ailuropoda microta",30,"female","extinct")
Panda4= Panda("Ailuropoda baconi",25,"female","extinct")

print(Panda1.type,Panda1.age,Panda1.gender,Panda1.extinct_or_alive)
print(Panda2.type,Panda2.age,Panda2.gender,Panda2.extinct_or_alive)
print(Panda3.type,Panda3.age,Panda3.gender,Panda3.extinct_or_alive)
print(Panda4.type,Panda4.age,Panda4.gender,Panda4.extinct_or_alive)


              