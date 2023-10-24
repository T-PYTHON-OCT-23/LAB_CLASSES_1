class Panda:
    def __init__(self,type,height,country,age,amount,hours):
        self.type=type
        self.height=height
        self.country=country
        self.age=age
        self.amount=amount
        self.hours=hours
    
    def walk(self):
        print(f'I am walking today for {self.amount} meters.')

    def sleep(self):
        print(f'I slept today for {self.hours} hours.')
print('\n')
Panda1=Panda('Ailuropoda microta','150','Saudi',23,22,15)
print('My type is',Panda1.type)
Panda1.walk()
Panda1.sleep()
print('-'*20)
Panda2=Panda('Ailuropoda wulingshanensis','123','America',15,20,33)
print('My type is',Panda2.type)
Panda2.walk()
Panda2.sleep()
print('-'*20)
Panda3=Panda('Ailuropoda baconi','170','Africa',30,10,20)
print('My type is',Panda3.type)
Panda3.walk()
Panda3.sleep()
print('-'*20)
Panda4=Panda('Ailuropoda melanoleuca','144','Saudi',20,6,23)
print('My type is',Panda4.type)
Panda4.walk()
Panda4.sleep()






    
