#normal
# squares1 = []
# for i in range(1,7):
#     squares1.append(i+1)
# print(squares1)

#list comprehension
squares2 = [i*i for i in range(1,7) if i % 2 == 1] #리스트 컴프레션에 홀수만 출력 조건 추가
print(squares2)

# a = {[2]: [1,2], "b" : (1,2)} #딕셔너리의 키 값은 불변이어야 한다. (set, list, dict 등등 불가능)
# print(type(a.get([2])))
#x = dict(fi rst="123",def="456") #딕셔너리의 키 값은 공백이나 예약어가 올 수 없다.