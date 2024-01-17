import random

drinks_foods = {"위스키" : "초콜릿", "와인" : "치즈", "소주" : "삼겹살", "고량주" : "양꼬치"}

# print(drinks_foods)
# print(drinks_foods.pop("고량주")) list에서는 pop사용시 ()형태로 사용할 수 있지만 딕셔너리에서는 ()에 키의 값을 넣어주어야 한다.
# print(drinks_foods)

#del drinks_foods["위스키"]
japan_drinks_foods = {"사케" : "광어회", "위스키" : "낙곱새"}
drinks_foods.update(japan_drinks_foods) #update 사용 시 겹치는 키가 있을 경우 ()안에 있는 딕셔너리의 벨류로 대체된다.
drinks_foods_keys = list(drinks_foods.keys())

# print(drinks_foods_keys)
# drinks_foods_keys.remove("위스키") # pop은 벨류값 반환하지만 remove는 하지 않음
# print(drinks_foods_keys)

#drink = input(drinks_foods.keys())
#print(drinks_foods[drink])

while True:
    menu = input(f'다음 술 중에 고르세요.\n1){drinks_foods_keys[0]} 2){drinks_foods_keys[1]}'
                 f' 3){drinks_foods_keys[2]} 4){drinks_foods_keys[3]} 5){drinks_foods_keys[4]} 6)아무거나 7)종료 : ')
    #random.choice(drinks_foods_keys)
    #menu = input(f'다음 술 중에 고르세요.\n{", ".join(drinks_foods_keys)}')
    if menu == '1':
        print(f'{drinks_foods_keys[0]}에 어울리는 안주는 {drinks_foods[drinks_foods_keys[0]]} 입니다.')
    elif menu == '2':
        print(f'{drinks_foods_keys[1]}에 어울리는 안주는 {drinks_foods[drinks_foods_keys[1]]} 입니다.')
    elif menu == '3':
        print(f'{drinks_foods_keys[2]}에 어울리는 안주는 {drinks_foods[drinks_foods_keys[2]]} 입니다.')
    elif menu == '4':
        print(f'{drinks_foods_keys[3]}에 어울리는 안주는 {drinks_foods[drinks_foods_keys[3]]} 입니다.')
    elif menu == '5':
        print(f'{drinks_foods_keys[4]}에 어울리는 안주는 {drinks_foods[drinks_foods_keys[4]]} 입니다.')
    elif menu == '6':
        random_drink = random.choice(drinks_foods_keys)
        print(f'{random_drink}에 어울리는 안주는 {drinks_foods[random_drink]} 입니다.')
    elif menu == '7':
        print("종료")
        break
