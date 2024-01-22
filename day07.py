#클래스에 속성을 할당할 수 있고 해당 속성은 자식 객체로 상속된다.
#자식 객체의 속성을 변경하면 클래스 속성에 영향을 미치지 않음, 나중에 클래스 속성을 변경해도 이미 생성한 자식객체에는 영향 미치지 않음
#클래스 메서드에서의 클래스 변수는 모든 객체에 영향을 미친다.

class FlyingBehavior:
    def fly(self):
        return '하늘을 날아갑니다.'
class JetPack(FlyingBehavior):
    def fly(self):
        return super().fly()


class Nofly(FlyingBehavior):
    def fly(self):
        return  '하늘을 날 수 없습니다.'

class FlyWithWings(FlyingBehavior):
    def fly(self):
        return super().fly()


class SwimmingBehavior:
    def swim(self):
        return print(f'{self.__name}이(가) 수영을 합니다.')

class Pokemon:
    def __init__(self,name,hp,fly):
        self.__name = name
        self.hp = hp
        self.fly_behavior = fly #aggregation (has-a)

    def attack(self):
        print("공격")
    @property #데코레이터, getter로 동작
    def name(self):
        return self.__name
    @name.setter #데코레이터, getter로 동작
    def name(self,new_name):
        self.__name = new_name

    #magic method
    def __str__(self): #print(객체) 하면 클래스 이름이 나왔었는데 매직 메서드를 이용하여 __name이 출력되게 바꿈
        return self.__name + "입니다."

    def __add__(self, other):
        #return self.name + " + " +other.name
        return f'두 포켓몬스터 체력의 합은 {self.hp + other.hp}입니다.'
    #name = property(get_name,set_name)
class Charizard(Pokemon):
    pass
class Pikachu(Pokemon):
    pass


nofly = Nofly()
p1 = Pikachu("피카츄",100,nofly)
wings = FlyingBehavior()
c1 = Charizard("리자몽",120,wings)
print(p1.fly.fly())
print(c1.fly.fly())
print(p1,c1)
print(p1+c1)