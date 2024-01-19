class FlyinMinin:
    def fly(self):
        return print(f'{self.hidden_name}이(가) 날아갑니다.')
class SwimmingMixin:
    def swim(self):
        return print(f'{self.hidden_name}이(가) 수영을 합니다.')
class Pokemon:
    def __init__(self,name):
        self.hidden_name = name
    def attack(self):
        print("공격")
    def get_name(self):
        print("inside getter")
        return self.hidden_name
    def set_name(self,new_name):
        print("inside setter")
        self.hidden_name = new_name

    name = property(get_name,set_name)
class Charizard(Pokemon, FlyinMinin):
    pass
class Gyarados(Pokemon, SwimmingMixin):
    pass

g1 = Gyarados("갸라도스")
c1 = Charizard("리자몽")
# g1.swim()
# c1.fly()
# c1.attack()
# #Charizard.attack() #에러. 이렇게 사용하기 위해서는 self에 해당하는 객체를 넣어주어야 함
# Charizard.attack(c1)
# print(g1.get_name())
# g1.set_name("잉어킹")
# print(g1.get_name())

#propertiy
print(g1.name)
g1.name = '잉어킹'
print(g1.hidden_name)