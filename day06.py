class Pokemon:
    #self : 실행시점의 객체의 메모리를 가지는 것을 의미한다.
    def __init__(self, name): #생성자, 객체 생성시 실행되는 함수 엄밀히 따지자면 생성자보단 초기화에 더 가깝다. __new__가 사실상 생성자임
        #is-a:상속관계
        #has-a:연관관계

        self.name = name
        print(f"{name} 포켓몬스터 생성")
    def attack(self, target):
        print(f'{self.name}이(가) {target.name}을(를) 공격!')

charizard = Pokemon("리자몽")
pikachu = Pokemon("피카츄")
squirtle = Pokemon("꼬부기")
charizard.attack(squirtle)
# pikachu.name = "피카츄"
# pikachu.nemesis = squirtle
# print(pikachu.name)
# #print(pikachu.nemesis.name)
# pikachu.nemesis.name = "꼬부기" #squirtle.name = "꼬부기"
# print(pikachu.nemesis.name)
# print(squirtle.name)

print(pikachu.name)
print(squirtle.name)