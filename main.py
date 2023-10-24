from Panda import Panda


lauz=Panda("Lauz",4,58,"Female",False)
sukkar=Panda("Sukkar",3,67,"Male",True)
yama=Panda("Yama",9,110,"Male",True)
lolo=Panda("Lolo",8,92,"Female",False)

lauz.intro()
sukkar.intro()
yama.intro()
lolo.intro()

print("----"*22)
lauz.awakness_statu()
lauz.awake()
lauz.awakness_statu()
print("----"*22)
sukkar.awakness_statu()
sukkar.sleep()
print("----"*22)
yama.sleep()
lolo.awake()