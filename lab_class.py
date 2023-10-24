class Panda:
    def __init__(self,name:str, color:str , age:int , gender:str) -> None:
        self.name = name
        self.color= color
        self.age = age
        self.gender = gender
        
    def info(self):
        info =f"It is name {self.name}, and it has {self.color} color , it is {self.age} years old , it is {self.gender}"
        return info
    
    def speed(self , speed:int):
        speed = f"It is runs at a speed of up to {speed} K/M"
        return speed
    
panda1 = Panda("Alisa","white",5,"Female")
panda2 = Panda("Bob","black",10,"male")
panda3 = Panda("Saodah","black",12,"Female")
panda4 = Panda("Mathat","white",15,"male")

print(f"panda2 , color is {panda2.color}")
print(panda1.info())
print(panda1.speed(5))