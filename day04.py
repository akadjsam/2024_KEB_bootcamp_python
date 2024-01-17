sugang = dict(python="kim",cpp="sung",db="kang")
# print(sugang)
# sugang['datastructure'] = 'kim'
# print(sugang)
# sugang['datastructure'] = 'park'
# print(sugang)
#
# print(sugang['db'])
# print(sugang.get("db")) # get으로 해당 키에 해당하는 벨류를 출력
# print(sugang.get("opensource")) #찾는 키값이 없으먼 none 리턴
# print(sugang.get("opensource", "not exist")) #찾는 키 값이 없으면 , 뒤의 값을 출력

for sub, professor in sugang.items(): #모든 키/벨류값을 가져온다.
    print(f'{sub} : {professor}') #딕셔너리에는 순서의 개념이 없다.

for i in sugang.keys(): #모든 키 가져오기 for i in sugang: 과 같게 동작한다.
    print(i)
for v in sugang.values(): #모든 벨류 가져오기
    print(v)

for s in sugang.items(): #하나로 받게 되면 튜플형태로 받는다.
    print(s) #튜플로 출력