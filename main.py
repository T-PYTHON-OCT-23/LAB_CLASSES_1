
class Panda:
    

    def __init__(self,color:str,spead:str,weigh:str,gender:str,age:str):
        
        self.color = color
        self.spead = spead
        self.weigh = weigh
        self.gender = gender
        self.age = age

    def intro(self):


        info={"color":self.color,"spead":self.spead,"weigh":self.weigh,"gender":self.gender,"age":self.age}

        return info
    
    
    def show_details(self,info):
        
        for k,v in info.items():
            print(f"{k} is {v}")




def pand1_info():
    print("this is pand1:")
    panda1=Panda("white and black","11km/h","90kg","male","3 years")
    age_panda1=panda1.intro()
    print(age_panda1["age"])
    panda1.show_details(panda1.intro())


def panda2_info():
    print("this is pand2:")
    panda2=Panda("white and black","12km/h","60kg","male","2 years")
    age_panda2=panda2.intro()
    print(age_panda2["age"])
    panda2.show_details(panda2.intro())

def pand3_info():
    print("this is pand3:")
    panda3=Panda("white and black","3km/h","20kg","female","1 month")
    age_panda3=panda3.intro()
    print(age_panda3["age"])
    panda3.show_details(panda3.intro())


def panda4_info():
    print("this is panda4:")
    panda4=Panda("white and black","14km/h","150kg","male","6 years")
    gender_panda4=panda4.intro()
    print(gender_panda4["gender"])
    panda4.show_details(panda4.intro())


pand1_info()

print("-"*20)

panda2_info()

print("-"*20)

pand3_info()

print("-"*20)

panda4_info()