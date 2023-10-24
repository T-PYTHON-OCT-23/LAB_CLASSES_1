class Panda:
    def __init__(self,name:str,age:str,gender:str,favorite_food:str):
        self.name = name
        self.gender= gender
        self.age=age
        self.favorite_food = favorite_food

    def eat(self):
        print(f"{self.name} is eating {self.favorite_food}.")  
         
    def sleep(self):
        print(f"{self.name} is sleeping.")

panda1 = Panda("Kiki", 5, "Female", "Bamboo")
panda2 = Panda("Momo", 3, "Male", "Apples")
panda3 = Panda("Lulu", 7, "Female", "Panda cake")
panda4 = Panda("Bobo", 8, "Male", "Carrots")
print(panda1.age)

panda1.eat()
panda1.sleep()

panda2.eat()
panda2.sleep()

panda3.eat()
panda3.sleep()

panda4.eat()
panda4.sleep()