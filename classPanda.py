class Panda:
     def __init__(self,name:str, age:int, country:str,   gender:str):
           self.name = name
           self.age = age
           self.gender = gender
           self.country =country
           

     def myPanda(self):
        introduction = f"Hi my panda name is {self.name}  , he is {self.age}  years old . As you can see it is a {self.gender}  "
        return introduction
     

     def myPandaCountry(self):
          introdu = f"   its from {self.country}"
          return introdu
          
panda1=Panda("PAPO" ,2," MALE" ,"SAUTH KOREA")

panda2=Panda("zac" ,3," MALE" ,"north KOREA")
panda3=Panda("lele" ,1 ," MALE","japan")
panda4=Panda("beto" ,6 ," MALE" ,"Dubai")



print(panda1.name, panda1.myPanda() , panda1.myPandaCountry() )
print(panda2.name, panda2.myPanda() , panda2.myPandaCountry()  )
print(panda3.name,panda3.myPanda() , panda3.myPandaCountry()  )
print(panda4.name, panda4.myPanda() , panda4.myPandaCountry()  )







