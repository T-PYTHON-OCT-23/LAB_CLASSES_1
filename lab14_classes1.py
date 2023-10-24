class Panda :
    def __init__(self, name:str , home:str,color:str,age:int) :
        self.name= name
        self.home = home
        self.color = color
        self.age = age

    def eat(self, feed:str):
       #self.feed = feed
       print(f"{self.name} eating a {feed}")
        

    def sleep(self, hours:int):
        print(f"{self.name} sleaping for {hours}")
         
    
    
Panda1 = Panda("Melanoleuca(Bob)","Central South China","Brown",20)
Panda2 = Panda("Ailurus fulgens(Bob)","Himalayas","Red",23)
Panda3 = Panda("Melanoleuca(Kiwi)","Central South China","Wight and Black",15)
Panda4 = Panda("Ailurus fulgens(Kiwi)","Himalayas","Wight and Black",23)   

'''print(Panda1.name , Panda1.home , Panda1.feed , Panda1.age)
print(Panda2.name , Panda2.home , Panda2.feed , Panda2.age)
print(Panda3.name , Panda2.home , Panda2.feed , Panda2.age)
print(Panda4.name , Panda2.home , Panda2.feed , Panda2.age)'''

print(Panda1.name)
print("\n --------------- \n")

Panda1.eat("bamboo")
Panda1.sleep(6)

Panda2.eat("apple")
Panda2.sleep(4)

Panda3.eat("leaves")
Panda3.sleep(10)

Panda1.eat("bamboo")
Panda1.sleep(15)

'''overfew =f"The name of panda is {self.name}, he lives in {self.home} ,feeds on {self.color} and his age is approximatly up to {self.age}."
        return(overfew)  
    '''