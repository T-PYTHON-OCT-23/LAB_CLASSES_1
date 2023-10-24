class Panda:
    def __init__(self, name:str, age:int, weight:int, gender:str, isAwake:bool):
        self.name=name
        self.age=age
        self.weight=weight
        self.gender=gender
        self.isAwake=isAwake
    
    def intro(self):
        print(self.name,"is my name,",self.age,"is my age,",self.weight,"is my weight,",self.gender,"is my gender")
        
    def awakness_statu(self):
        print(f"is {self.name} awake? answer: {self.isAwake}")

    def awake(self):
        self.isAwake=True
        print(f"Good morning, my name is {self.name} and I just woke up")
        
    def sleep(self):
        print(f"Good night, my name is {self.name} and I'm going to sleep")
        self.isAwake=False