from os import name


class FlyinMinin:
    def fly(self):
        return print(f'{self.__name}이(가) 날아갑니다.')
class SwimmingMixin:
    def swim(self):
        return print(f'{self.__name}이(가) 수영을 합니다.')
class Pokemon:
    def __init__(self,name):
        self.__name = name
    def attack(self):
        print("공격")

    @property #데코레이터, getter로 동작
    def name(self):
        return self.__name
    @name.setter #데코레이터, getter로 동작
    def name(self,new_name):
        self.__name = new_name

    #name = property(get_name,set_name)
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
# print(g1.name)
# g1.hidden_name = '잉어킹'
# print(g1.name)

print(g1.name)
#print(g1.__name) #direct access x 파이썬은 private기능이 없지만 최대한 우회할 수 있다.
g1.__name = '잉어킹'
print(g1._Pokemon__name) #사실상 private는 지원하지 않음