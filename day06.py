class FlyinMinin:
    def fly(self):
        return print(f'{self.name}이(가) 날아갑니다.')
class SwimmingMixin:
    def swim(self):
        return print(f'{self.name}이(가) 수영을 합니다.')
class Pokemon:
    def __init__(self,name):
        self.name = name

class Charizard(Pokemon, FlyinMinin):
    pass
class Gyarados(Pokemon, SwimmingMixin):
    pass

g1 = Gyarados("갸라도스")
c1 = Charizard("리자몽")
g1.swim()
c1.fly()