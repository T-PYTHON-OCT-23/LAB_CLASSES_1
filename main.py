class Panda:

    def __init__(self,color:str,type:str,is_rare:str,gender:str,left:int):
        self.color = color
        self.type = type
        self.is_rare = is_rare
        self.gender = gender
        self.left = left
    
    def information(self):
        info = f"This panda is a {self.color}, from {self.type} family and have a {self.gender} gender"
        return info
    
    def is_rarea(self):
        rare = f"is this panda is rare? {self.is_rare} and only {self.left} left in wearth"
        return rare


panda1 = Panda("white","Domodoma","Yes, and from rarest family","male",15)
panda2 = Panda("black-white","DomoBora","No, have a lot of his kind","female",123412)

print(Panda.information(panda1))
print(Panda.is_rarea(panda1))
print("#"*24)
print(Panda.information(panda2))
print(Panda.is_rarea(panda2))



