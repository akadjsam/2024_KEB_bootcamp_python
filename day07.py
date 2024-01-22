#클래스에 속성을 할당할 수 있고 해당 속성은 자식 객체로 상속된다.
#자식 객체의 속성을 변경하면 클래스 속성에 영향을 미치지 않음, 나중에 클래스 속성을 변경해도 이미 생성한 자식객체에는 영향 미치지 않음
#클래스 메서드에서의 클래스 변수는 모든 객체에 영향을 미친다.

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

    def __str__(self): #print(객체) 하면 클래스 이름이 나왔었는데 매직 메서드를 이용하여 __name이 출력되게 바꿈
        return self.__name + "입니다."

    def __add__(self, other):
        return self.name + " + " +other.name
    #name = property(get_name,set_name)
class Charizard(Pokemon, FlyinMinin):
    pass
class Gyarados(Pokemon, SwimmingMixin):
    pass

g1 = Gyarados("갸라도스")
c1 = Charizard("리자몽")
print(g1,c1)
print(g1+c1)