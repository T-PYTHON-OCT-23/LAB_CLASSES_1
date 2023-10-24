class Panda:

    def __init__(self , hight:float , weight:float , type:str , age: int):
        self.hight = hight
        self.weight = weight
        self.type = type
        self.age = age

    def lazy(self , is_lazy:bool ):
        return True
    
    def Senseـofـsmelling(self , smelling:bool):
        #sense of smelling so good in panda
        return True



panda1 = Panda(1.5 , 150.0 , "Wild" , 30 ) 
panda2 = Panda(1.8 , 155.4 , "Polar" , 28 ) 
panda3 = Panda(1.3 , 158.0 , "Wild" , 25 ) 
panda4 = Panda(1.9 , 160.5 , "Polar" , 31 ) 

print("\n informaion of panda : \n " , panda1.hight , panda1.weight , panda1.type , panda1.age)
print("\n is the panda lazy animal ? \n ",panda1.lazy(True))
print("\n is the panda have a strong sense of smilling ?\n ",panda1.Senseـofـsmelling(True))

print("\n informaion of panda : \n " , panda2.hight , panda2.weight , panda2.type , panda2.age)
print("\n is the panda lazy animal ? \n ",panda2.lazy(True))
print("\n is the panda have a strong sense of smilling ?\n ",panda2.Senseـofـsmelling(True))

print("\n informaion of panda : \n " , panda3.hight , panda3.weight , panda3.type , panda3.age)
print("\n is the panda lazy animal ? \n ",panda3.lazy(True))
print("\n is the panda have a strong sense of smilling ?\n ",panda3.Senseـofـsmelling(True))


print("\n informaion of panda : \n " , panda4.hight , panda4.weight , panda4.type , panda4.age)
print("\n is the panda lazy animal ? \n ",panda4.lazy(True))
print("\n is the panda have a strong sense of smilling ?\n ",panda4.Senseـofـsmelling(True))