class Panda:

    def __init__(self, color:str, height:int, weight:int, name:str):
        
        self.color = color 
        self.height = height
        self.weight = weight
        self.name = name

    def information(self):
        return f" my color is {self.color}" 

    def pandaBody(self):
        return f"My height is {self.height} and my weight is {self.weight}"  

panda1 = Panda("white and black", 159 , 120 , "loly")
panda2 = Panda("white and black", 170 , 125 , "lily")
panda3 = Panda("white and black", 140 , 115 , "bao")
panda4 = Panda("white and black", 150 , 130 , "koki")



print(f"Hello i am {panda1.name}, {panda1.information()}, {panda1.pandaBody()}")
print(f"Hello i am {panda2.name}, {panda2.information()}, {panda2.pandaBody()}")
print(f"Hello i am {panda3.name}, {panda3.information()}, {panda3.pandaBody()}")
print(f"Hello i am {panda4.name}, {panda4.information()}, {panda4.pandaBody()}")
