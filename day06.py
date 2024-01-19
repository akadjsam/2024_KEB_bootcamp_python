class Pokemon:
    def __init__(self,name):
        self.name = name
    def attack(self,target):
        print(f'{self.name}이(가) {target.name}을(를) 공격!')

class Pikachu(Pokemon): #is-a 상속관계
    def __init__(self, name, type):
        super().__init__(name)
        self.type = type

    def attack(self, target):
        print(f'{self.name}이(가) {target.name}에게 {self.type} 공격!')
    # def electric_info(self):
    #     print("전기계열의 공격을 실행")

class Squirtle(Pokemon): #is-a 상속관계
    pass #메서드 오버라이드 하지 않고 사용하면 부모의 메서드를 찾아가서 사용한다.
    #def attack(self, target):
        #print(f'{self.name}이(가) {target.name}에게 전기 공격!')

class Agumon:
    pass

p1 = Pikachu("피카츄", "전기")
s1 = Squirtle("꼬부기")
#p3 = Pokemon("아무개")
#p3.electric_info() #자식의 메서드를 사용하지 못한다.
p1.attack(s1)
s1.attack(p1)
print(p1.name,p1.type)
print(issubclass(Pikachu, Pokemon))
print(issubclass(Agumon, Pokemon)) #상속관계인지 확인할 때 사용한다. (boolean type)