import random

drinks_foods = {"위스키" : "초콜릿", "와인" : "치즈", "소주" : "삼겹살", "고량주" : "양꼬치"}
drinks_foods_keys = list(drinks_foods.keys())
#drink = input(drinks_foods.keys())
#print(drinks_foods[drink])

while True:
    menu = input(f'다음 술 중에 고르세요.\n1){drinks_foods_keys[0]}, 2){drinks_foods_keys[1]},'
                 f' 3){drinks_foods_keys[2]}, 4){drinks_foods_keys[3]}, 5)아무거나 6)종료 : ')
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
        random_drink = random.choice(drinks_foods_keys)
        print(f'{random_drink}에 어울리는 안주는 {drinks_foods[random_drink]} 입니다.')
    elif menu == '6':
        print("종료")
        break
