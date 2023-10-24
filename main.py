class Panda:
    def __init__(self,Type,HomeNation,yearBirth,gender) -> None:
        self.Type = Type
        self.HomeNation = HomeNation
        self.yearBirth = int(yearBirth)
        self.gender = gender
        self.age =0
    def CalculateAge(self):
        self.age = 2023 - self.yearBirth
        return self.age
    def __str__(self) -> str:
        return f"{self.Type}--{self.HomeNation}--{self.age}--{self.gender}"



panda1 = Panda("Red panda","China",2020,"male")
panda2 = Panda("Giant panda","Russia",2019,"Female")
panda3 = Panda("Giant panda","Russia",2015,"male")
panda4 = Panda("Qinling panda","China",2000,"male")


print(f"Panda age is:{panda1.CalculateAge()}")
print(panda1.__str__())
print(f"Panda age is:{panda2.CalculateAge()}")
print(panda2.__str__())
print(f"Panda age is:{panda3.CalculateAge()}")
print(panda3.__str__())
print(f"Panda age is:{panda4.CalculateAge()}")
print(panda4.__str__())