class Pokemon:
    def __init__(self, name): #생성자, 객체 생성시 실행되는 함수
        self.name = name
        print(f"{name} 포켓몬스터 생성")

pikachu = Pokemon("피카츄")
squirtle = Pokemon("꼬부기")